
def file_to_dict(filename):
    phone_number_costs = {}
    with open(filename, 'r') as file:
        for line in file:
            (key, value) = line.strip('\n').split(',')
            if key not in phone_number_costs.keys():
                phone_number_costs[key] = value
    return phone_number_costs

def find_route_cost(routes_list,phone_numbers):
    routes_and_costs = file_to_dict(routes_list)
    phone_numbers = open(phone_numbers,'r')
    for line in phone_numbers:
        number = line.strip('\n')
        phone_number = number
        while len(number) > 1:
            if number in routes_and_costs.keys():
                print('phone number: {} Cost: {}'.format(phone_number, routes_and_costs[number]))
                break
            number = number[:-1]
    print('Number not found')


if __name__ == '__main__':

    find_route_cost('route-costs-106000.txt', 'phone-numbers-1000.txt')
