from random import random
from models.customers import *
from algorithms.greedy import run as run_greedy
from time import perf_counter


def geometric_decrement(T):
    alpha = 0.98
    return T * alpha

def slow_decrease(T):
    beta = 0.001
    return T / (1 + beta * T)

T0 = 1000
decrement_function = slow_decrease
T_final = 0.001
delta_correction_factor = 1000

def advance_neighbourhood(routes: [[Customer]], depot: Customer, customers: [Customer], capacity: int, T: int) -> [
    [[Customer]]]:
    new_routes = generate_neighbour(routes, depot, customers, capacity)
    old_quality = return_solution_quality(depot, routes)
    new_quality = return_solution_quality(depot, new_routes)

    delta = new_quality[1] - old_quality[1] + delta_correction_factor
    if new_quality < old_quality or random() < math.exp(-delta/T):
        return new_routes

    return routes


def run(
        depot: Customer,
        customers: [Customer],
        vehicle_count: int,
        capacity: int,
        routes: [[[Customer]]],
        time_limit: float = math.inf,
        verbose=False
) -> [[Customer]]:
    start_time = perf_counter()
    iterations = 0

    since_last_improvement = 0
    reheat = 0
    T = T0
    T_best = T0
    best_score = return_solution_quality(depot, routes)
    best_routes = routes
    stop_reheating = False
    while T > T_final:
        if verbose:
            print(best_score)

        new_routes = advance_neighbourhood(routes, depot, customers, capacity, T)
        iterations += 1
        since_last_improvement += 1

        score = return_solution_quality(depot,new_routes)
        if score < best_score:
            best_score = score
            best_routes = new_routes
            T_best = T
            since_last_improvement = 0

        T = decrement_function(T)

        if since_last_improvement > 100 and stop_reheating is False:
            if reheat > 5:
                # print('STOP')
                stop_reheating = True
            # print('RESTART')
            routes = best_routes
            T = T_best
            since_last_improvement = 0
            reheat += 1

    return best_routes,best_score
