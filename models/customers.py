import math


class Customer:
    def __init__(
            self,
            identifier: int,
            x: float,
            y: float,
            demand: float,
            ready_time: float,
            due_date: float,
            service_time: float
    ):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time

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
    if time_of_arrival < customer.ready_time:
        time_of_arrival = customer.ready_time
    return time_of_arrival
