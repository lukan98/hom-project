from models.customers import *
from time import perf_counter


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

    best_quality = math.inf, math.inf
    best_solution = None

    while (quality := return_solution_quality(depot, routes)) < best_quality and \
            perf_counter() - start_time <= time_limit:
        best_quality = quality
        best_solution = routes
        neighbours = generate_neighbours_greedy(routes, depot, customers, capacity)

        if len(neighbours) > 0:
            routes = neighbours[0]
            iterations += 1
        else:
            break

        if verbose:
            print(f'Iteration: {iterations}, best solution quality: {best_quality}')

    return best_solution
