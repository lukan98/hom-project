from models.customers import *
from algorithms.greedy import run as run_greedy
from math import inf
from instanceio.output import *


def run(
        depot: Customer,
        customers: [Customer],
        vehicle_count: int,
        capacity: int
) -> [[Customer]]:
    routes = run_greedy(depot, customers, vehicle_count, capacity)
    best_quality = math.inf, math.inf
    best_solution = None

    iters = 0
    while (quality := return_solution_quality(depot, routes)) < best_quality:
        best_quality = quality
        best_solution = routes
        neighbours = generate_neighbours(routes, depot, customers, capacity)[0]

        if len(neighbours) > 0:
            routes = neighbours[0]
            iters += 1
        else:
            break
        print(f'iter: {iters} best quality: {best_quality}')

    print_solution(depot, best_solution)
    print(iters)