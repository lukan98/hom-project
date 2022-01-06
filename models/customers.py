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
        distance += calculate_distance(route[i-1], route[i])
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
