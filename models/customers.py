import math
from dataclasses import dataclass


@dataclass
class Customer:
    identifier: int
    x: int
    y: int
    demand: int
    ready_time: int
    due_date: int
    service_time: int

    def __str__(self):
        return self.demand, self.ready_time, self.due_date, self.service_time

    def interval_of_service(self) -> (float, float):
        return self.ready_time, self.due_date


def calculate_distance(a: Customer, b: Customer) -> float:
    x_difference = math.pow(abs(a.x - b.x), 2)
    y_difference = math.pow(abs(a.y - b.y), 2)

    return math.sqrt(x_difference + y_difference)


def calculate_time_of_arrival(
        customer: Customer,
        prev_time_of_arrival: float,
        prev_customer: Customer
) -> float:
    time_of_arrival = prev_time_of_arrival + prev_customer.service_time + calculate_distance(customer, prev_customer)
    time_of_arrival = math.ceil(time_of_arrival)

    if time_of_arrival < customer.ready_time:
        time_of_arrival = customer.ready_time
    return time_of_arrival


def calculate_route_length(depot: Customer, route: [Customer]):
    distance = 0
    distance += calculate_distance(depot, route[0])
    for i in range(1, len(route)):
        distance += calculate_distance(route[i - 1], route[i])
    distance += calculate_distance(route[-1], depot)
    return distance


def sort_by_time_of_arrival(current_customer: Customer, customers: [Customer], prev_time_of_arrival: int):
    return sorted(customers,
                  key=lambda other_customer: calculate_time_of_arrival(other_customer,
                                                                       prev_time_of_arrival,
                                                                       current_customer))


def filter_viable_customers(
        current_customer: Customer,
        depot: Customer,
        customers: [Customer],
        prev_time_of_arrival: int,
        current_capacity: int
) -> [Customer]:
    capacity_filter = filter((lambda customer:
                              customer.demand <= current_capacity),
                             customers)
    due_date_filter = filter((lambda customer:
                              calculate_time_of_arrival(customer,
                                                        prev_time_of_arrival,
                                                        current_customer) <= customer.due_date),
                             capacity_filter)
    distance_filter = filter((lambda customer:
                              calculate_time_of_arrival(depot,
                                                        calculate_time_of_arrival(customer,
                                                                                  prev_time_of_arrival,
                                                                                  current_customer),
                                                        customer) <= depot.due_date),
                             due_date_filter)

    return list(distance_filter)


def check_route_demand_validity(route: [Customer], capacity: int) -> bool:
    return sum(map(lambda customer: customer.demand, route)) <= capacity


def check_scheduling_validity(depot: Customer, route: [Customer]) -> bool:
    time_of_arrival = 0
    time_of_arrival = calculate_time_of_arrival(route[0], time_of_arrival, depot)

    if time_of_arrival > route[0].due_date:
        return False
    if time_of_arrival + calculate_time_of_arrival(depot, time_of_arrival, route[0]) > depot.due_date:
        return False

    for i in range(1, len(route)):
        time_of_arrival = calculate_time_of_arrival(route[i], time_of_arrival, route[i - 1])

        if time_of_arrival > route[i].due_date:
            return False
        if calculate_time_of_arrival(depot, time_of_arrival, route[i]) > depot.due_date:
            return False

    if calculate_time_of_arrival(depot, time_of_arrival, route[-1]) > depot.due_date:
        return False

    return True


def check_route_validity(depot: Customer, route: [Customer], capacity: int) -> bool:
    return check_route_demand_validity(route, capacity) and check_scheduling_validity(depot, route)


def insert_customer_into_route(depot: Customer, customer: Customer, route: [Customer], capacity: int) -> [[Customer]]:
    generated_routes = []
    for i in range(len(route)):
        modified_route = route.copy()
        modified_route.insert(i, customer)
        if check_route_validity(depot, modified_route, capacity):
            generated_routes.append(modified_route)
    return generated_routes


def find_route_by_customer(customer: Customer, routes: [[Customer]]) -> int:
    for i, route in enumerate(routes):
        if customer in route:
            return i


def sum_all_customers(routes: [[Customer]]):
    sum = 0
    for route in routes:
        sum += len(route)
    return sum


def return_solution_quality(depot: Customer, routes: [[Customer]]) -> (int, float):
    nr_vehicles = len(routes)
    distance = sum(map(lambda route: calculate_route_length(depot, route), routes))
    return nr_vehicles, distance

def generate_neighbours(routes: [[Customer]], depot:Customer, customers: [Customer], capacity: int):

    neighbours = []
    neighbours_quality = []

    for route in routes:
        customers_not_in_route = list(filter(lambda c: c not in route, customers))
        for customer in customers_not_in_route:
            generated_routes = insert_customer_into_route(depot, customer, route, capacity)
            if len(generated_routes) != 0:
                for generated_route in generated_routes:
                    old_route_index = find_route_by_customer(customer, routes)
                    new_routes = [route[:] for route in routes]
                    new_routes[old_route_index].remove(customer)
                    if len(new_routes[old_route_index]) == 0:
                        new_routes.remove(new_routes[old_route_index])
                    new_routes[routes.index(route)] = generated_route
                    neighbours.append(new_routes)
                    neighbours_quality.append(return_solution_quality(depot, new_routes))

    sorted_neighbours = sorted(neighbours, key=(lambda neighbor: (neighbours_quality[neighbours.index(neighbor)][0],
                                                                  neighbours_quality[neighbours.index(neighbor)][1])))

    return sorted_neighbours,neighbours_quality