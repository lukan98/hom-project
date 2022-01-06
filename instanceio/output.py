from models.customers import Customer, calculate_time_of_arrival, calculate_route_length


SOLUTIONS_PATH = './resources/solutions/i'


def get_solution_string(depot: Customer, routes: [[Customer]]) -> str:
    total_distance = 0
    solution_string = f'{len(routes)}\n'

    for route_index, route in enumerate(routes):
        prev_time = 0

        solution_string += f'{route_index + 1}: '
        solution_string += '0(0)'

        time_of_arrival = calculate_time_of_arrival(route[0], prev_time, depot)
        solution_string += f'->{route[0].identifier}({time_of_arrival})'
        prev_time = time_of_arrival

        for i in range(1, len(route)):
            time_of_arrival = calculate_time_of_arrival(route[i], prev_time, route[i - 1])
            solution_string += f'->{route[i].identifier}({time_of_arrival})'
            prev_time = time_of_arrival

        time_of_arrival = calculate_time_of_arrival(depot, prev_time, route[-1])
        solution_string += f'->{depot.identifier}({time_of_arrival})'

        solution_string += '\n'
        total_distance += calculate_route_length(depot, route)

    solution_string += str(total_distance)
    return solution_string


def print_solution(depot: Customer, routes: [[Customer]]):
    print(get_solution_string(depot, routes))


def write_solution(index: int, depot: Customer, routes: [[Customer]]):
    with open(f'{SOLUTIONS_PATH}{index}.txt', 'w') as file:
        file.write(get_solution_string(depot, routes))
