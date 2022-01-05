from models.customers import *


customers = []
vehicles = []

def sort_by_distance(customer):
    sorted_customers = sorted(customers, key=lambda other_customer:calculate_distance(customer,other_customer))
    return sorted_customers

with open('./resources/instances/i1.txt', 'r', encoding='latin-1') as file:
    for index,line in enumerate(file):
        if index == 2: #vehicles and capacities
            vehicles,capacity = [int(i) for i in line.split()]
        elif index == 7:
            identifier,x,y,demand,ready_time,due_date,service_time = [int(i) for i in line.split()]
            depot = Customer(identifier,x,y,demand,ready_time,due_date,service_time)

        elif index > 7:
            identifier,x,y,demand,ready_time,due_date,service_time = [int(i) for i in line.split()]
            customer = Customer(identifier,x,y,demand,ready_time,due_date,service_time)
            customers.append(customer)

customers.sort(reverse=True)
#customers = sorted(customers,key=lambda customer:customer.due_date)
customers = sorted(customers,key=lambda customer:customer.ready_time)
print(customers)

sorted_customers = sort_by_distance(depot)
print(customers)




