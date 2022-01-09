from models.customers import *
from time import perf_counter


def run(
        depot: Customer,
        customers: [Customer],
        vehicle_count: int,
        capacity: int,
        routes: [[[Customer]]],
        neighbour_sorting_fn,
        patience_limit: int = 100,
        time_limit: float = math.inf,
        verbose=False
) -> ([[Customer]], int):
    start_time = perf_counter()
    iterations = 0
    patience = 0

    best_quality = math.inf, math.inf
    best_solution = None

    while (quality := return_solution_quality(depot, routes)) < best_quality and \
            perf_counter() - start_time <= time_limit:

        if quality < best_quality:
            best_quality = quality
            best_solution = routes

        neighbours = neighbour_sorting_fn(routes, depot, customers, capacity)
        better_neighbours = list(filter(lambda neighbour: return_solution_quality(depot, neighbour) <= best_quality,
                                        neighbours))

        iterations += 1
        if len(better_neighbours) > 0:
            routes = better_neighbours[0]
            patience = 0
        elif patience < patience_limit and len(neighbours) > 0:
            routes = neighbours[0]
            patience += 1
        else:
            break

        if verbose:
            print(f'Iteration: {iterations}, best solution quality: {best_quality}')

    return best_solution, iterations
