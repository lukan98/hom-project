from models.customers import *


customers = []
vehicles = []

def sort_by_distance(customer,customer_list):
    sorted_customers = sorted(customer_list, key=lambda other_customer:calculate_distance(customer,other_customer))
    return sorted_customers

def filter_viable(neighbours, current_point,current_time, current_capacity, depot):
    distance_filter = filter((lambda n: calculate_time_of_arrival(depot,calculate_time_of_arrival(n,current_time,current_point),n) <= depot.due_date),neighbours)
    capacity_filter = filter((lambda n: n.demand <= current_capacity),distance_filter)
    return list(capacity_filter)

def print_solution(route):
    route.append(depot)
    route.insert(0,depot)
    prev_time = 0
    for i in range(1,len(route)):
        new_time = calculate_time_of_arrival(route[i],prev_time,route[i-1])
        print('time: ',new_time)
        prev_time = new_time








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

#customers = sorted(customers,key=lambda customer:customer.due_date)
#customers = sorted(customers,key=lambda customer:customer.ready_time)

remaining_customers = customers.copy()
#remaining_list = [customer.identifier for customer in customers]
current_customer = depot
current_time = 0
current_capacity = capacity
route = []
while len(remaining_customers) > 0:

    remaining_customers = sort_by_distance(current_customer,remaining_customers)
    filtered = filter_viable(remaining_customers, current_customer, current_time, current_capacity, depot)

    if len(filtered) > 0:
        chosen = filtered[0]
        route.append(chosen)
        remaining_customers.remove(chosen)
        current_time += calculate_time_of_arrival(chosen, current_time, current_customer)
        current_customer = chosen
        current_capacity -= chosen.demand
    else:
        print('done')
        break


print(route)
print_solution(route)








