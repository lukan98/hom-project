from models.customers import Customer

INSTANCES_PATH = './resources/instances/i'
ENCODING = 'latin-1'


def parse_instance(index: int) -> (Customer, [Customer], int, int):
    with open(f'{INSTANCES_PATH}{index}.txt', 'r', encoding=ENCODING) as file:
        customers = []

        for index, line in enumerate(file):
            if index == 2:  # vehicles and capacities
                vehicle_count, capacity = [int(i) for i in line.split()]
            elif index == 7:
                identifier, x, y, demand, ready_time, due_date, service_time = [int(i) for i in line.split()]
                depot = Customer(identifier, x, y, demand, ready_time, due_date, service_time)

            elif index > 7:
                identifier, x, y, demand, ready_time, due_date, service_time = [int(i) for i in line.split()]
                customer = Customer(identifier, x, y, demand, ready_time, due_date, service_time)
                customers.append(customer)

    return depot, customers, vehicle_count, capacity
