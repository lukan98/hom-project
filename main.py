from algorithms.greedy import run as run_greedy
from instanceio.input import parse_instance
from instanceio.output import write_solution, print_solution


INSTANCE_INDEX = 1
depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
routes = run_greedy(depot, customers, vehicle_count, capacity)

print_solution(depot, routes)
write_solution(INSTANCE_INDEX, depot, routes)