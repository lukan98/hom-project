from algorithms.greedy import run as run_greedy
from instanceio.input import parse_instance
from instanceio.output import write_solution, print_solution
from models.customers import *

INSTANCE_INDEX = 1
depot, customers, vehicle_count, capacity = parse_instance(INSTANCE_INDEX)
routes = run_greedy(depot, customers, vehicle_count, capacity)

print_solution(depot, routes)
write_solution(INSTANCE_INDEX, depot, routes)

initial_quality = return_solution_quality(depot,routes)
successes = []
neighbours = []
neighbours_quality = []
hits = 0
for route in routes:

    customers_not_in_route = list(filter(lambda c: c not in route, customers))
    for customer in customers_not_in_route:
        generated_routes = insert_customer_into_route(depot, customer, route, capacity)
        if len(generated_routes) > 1:
            hits+=1
        if len(generated_routes) != 0:
            for generated_route in generated_routes:
                old_route_index = find_route_by_customer(customer,routes)
                new_routes = [route[:] for route in routes]
                new_routes[old_route_index].remove(customer)
                if len(new_routes[old_route_index]) == 0:
                    new_routes.remove(new_routes[old_route_index])
                new_routes[routes.index(route)] = generated_route
                neighbours.append(new_routes)
                neighbours_quality.append(return_solution_quality(depot,new_routes))

print(len(neighbours))
print(hits)

sorted_neighbours = sorted(neighbours, key=(lambda neighbor:(neighbours_quality[neighbours.index(neighbor)][0],
                                            neighbours_quality[neighbours.index(neighbor)][1])))

print_solution(depot,sorted_neighbours[0])
print("done")

for customer in customers:
    route = find_route_by_customer(customer, sorted_neighbours[0])
    if route is None:
        print(find_route_by_customer(customer, routes))
        print(customer.identifier)
