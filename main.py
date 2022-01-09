from instanceio.input import parse_instance
from instanceio.output import write_solution
from algorithms.local import run as run_local
from algorithms.greedy import run as run_greedy


INSTANCE_INDEX = 6
TIME_LIMIT = 20

depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
greedy_solution = run_greedy(depot, customers, vehicle_count, capacity)
local_solution = run_local(depot, customers, vehicle_count, capacity, greedy_solution, time_limit=TIME_LIMIT * 60)

write_solution(INSTANCE_INDEX, depot, local_solution, time_limit=TIME_LIMIT)
