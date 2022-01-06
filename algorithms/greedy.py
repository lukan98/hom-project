from models.customers import *


def run(
        depot: Customer,
        customers: [Customer],
        vehicle_count: int,
        capacity: int
) -> [[Customer]]:
    routes = []
    remaining_customers = customers.copy()
    current_customer = depot
    current_time = 0
    current_capacity = capacity
    route = []
    nr_routes = 0

    while len(remaining_customers) > 0:
        remaining_customers = sort_by_time_of_arrival(current_customer, remaining_customers, current_time)
        viable_customers = filter_viable_customers(current_customer,
                                                   depot,
                                                   remaining_customers,
                                                   current_time,
                                                   current_capacity)

        if len(viable_customers) > 0:
            chosen = viable_customers[0]
            route.append(chosen)
            remaining_customers.remove(chosen)
            current_time = calculate_time_of_arrival(chosen, current_time, current_customer)
            current_customer = chosen
            current_capacity -= chosen.demand
        else:
            nr_routes += 1
            routes.append(route.copy())
            route = []
            current_capacity = capacity
            current_time = 0
            current_customer = depot

    routes.append(route)
    return routes
