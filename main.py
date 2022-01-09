from instanceio.input import parse_instance
from instanceio.output import write_solution
from algorithms.local import run as run_local
from algorithms.greedy import run as run_greedy
from algorithms.new_heuristic_test import run as run_new_heuristic
from instanceio.output import print_solution


INSTANCE_INDEX = 1
TIME_LIMIT = 20

depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
#greedy_solution = run_greedy(depot, customers, vehicle_count, capacity)
#local_solution = run_local(depot, customers, vehicle_count, capacity, greedy_solution, time_limit=TIME_LIMIT * 60)
new_heuristic_solution = run_new_heuristic(depot,customers,vehicle_count, capacity)

print_solution(depot,new_heuristic_solution)


#write_solution(INSTANCE_INDEX, depot, local_solution, time_limit=TIME_LIMIT)
