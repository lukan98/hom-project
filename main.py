from models.customers import *

a = Customer(identifier=0, x=35, y=35, demand=0, ready_time=0, due_date=230, service_time=0)
b = Customer(identifier=1, x=41, y=49, demand=10, ready_time=0, due_date=204, service_time=10)

print(calculate_distance(a, b))
