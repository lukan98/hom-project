from algorithms.greedy import run as run_greedy
from instanceio.input import parse_instance
from instanceio.output import write_solution, print_solution
from models.customers import insert_customer_into_route


INSTANCE_INDEX = 1
depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
routes = run_greedy(depot, customers, vehicle_count, capacity)

print_solution(depot, routes)
write_solution(INSTANCE_INDEX, depot, routes)

successes = []
for route in routes:
    customers_not_in_route = list(filter(lambda c: c not in route, customers))
    for customer in customers_not_in_route:
        generated_routes = insert_customer_into_route(depot, customer, route, capacity)
        if len(generated_routes) != 0:
            for generated_route in generated_routes:
                successes.append(generated_route)

print(len(successes))