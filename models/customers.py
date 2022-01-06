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

    def __lt__(self, other):
        if self.due_date == other.due_date:
            return self.ready_time < other.ready_time
        return self.due_date < other.due_date

    def interval_of_service(self) -> (float, float):
        return self.ready_time, self.due_date


def calculate_distance(a: Customer, b: Customer) -> float:
    x_difference = math.pow(abs(a.x - b.x), 2)
    y_difference = math.pow(abs(a.y - b.y), 2)

    return math.sqrt(x_difference + y_difference)


def calculate_time_of_arrival(
        customer: Customer,
        prev_time_of_arrival: float = 0,
        prev_customer: Customer = None
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
