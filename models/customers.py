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


def calculate_distance(a: Customer, b: Customer) -> float:
    x_difference = math.pow(abs(a.x - b.x), 2)
    y_difference = math.pow(abs(a.y - b.y), 2)

    return math.sqrt(x_difference + y_difference)
