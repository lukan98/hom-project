from instanceio.input import parse_instance
from instanceio.output import write_solution, print_solution
from algorithms.local import run as run_local
from algorithms.heuristic import run as run_heuristic
from algorithms.greedy import run as run_greedy
from algorithms.SA import run as run_sa
from models.customers import generate_neighbours_heuristic, return_solution_quality


INSTANCE_INDEX = 7
TIME_LIMIT = 1

depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
greedy_solution = run_greedy(depot, customers, vehicle_count, capacity)

print_solution(depot, greedy_solution)

local_solution, local_iterations = run_local(depot=depot,
                                             customers=customers,
                                             vehicle_count=vehicle_count,
                                             capacity=capacity,
                                             routes=greedy_solution,
                                             time_limit=TIME_LIMIT * 60,
                                             verbose=True)

heuristic_solution, heuristic_iterations = run_heuristic(depot=depot,
                                                         customers=customers,
                                                         vehicle_count=vehicle_count,
                                                         capacity=capacity,
                                                         routes=greedy_solution,
                                                         neighbour_sorting_fn=generate_neighbours_heuristic,
                                                         patience_limit=500,
                                                         time_limit=TIME_LIMIT * 60,
                                                         verbose=True)

local_solution_quality = return_solution_quality(depot, local_solution)
custom_heuristic_quality = return_solution_quality(depot, heuristic_solution)

print('LOCAL SOLUTION BETTER' if local_solution_quality < custom_heuristic_quality else 'CUSTOM HEURISTIC BETTER')
best_solution = local_solution if local_solution_quality < custom_heuristic_quality else heuristic_solution
best_iterations = local_iterations if local_solution_quality < custom_heuristic_quality else heuristic_iterations

write_solution(INSTANCE_INDEX, depot, best_solution, best_iterations, time_limit=TIME_LIMIT)
SA_solution = run_sa(depot,
                     customers,
                     vehicle_count,
                     capacity,
                     greedy_solution,
                     time_limit=TIME_LIMIT * 60,
                     verbose=True)
print_solution(depot,SA_solution[0])
