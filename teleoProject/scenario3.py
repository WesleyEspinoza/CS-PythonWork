
def file_to_dict(filename):
    phone_number_costs = {}
    with open(filename, 'r') as file:
        for line in file:
            (key, value) = line.strip('\n').split(',')
            if key not in phone_number_costs.keys():
                phone_number_costs[key] = value
    return phone_number_costs

def file_to_numbers(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            number = line.strip('\n')
            numbers.append(number)
        return numbers


def find_route_cost(route_lists,phone_numbers_list):
    list_of_dicts = []
    list_of_Phone_numbers = []
    list_of_found_routes = []


    for route_list in route_lists:
        list_of_dicts.append(file_to_dict(route_list))
        print('finished routes')

    for phone_numbers in phone_numbers_list:
        list_of_Phone_numbers.append(file_to_numbers(phone_numbers))
        print('finished phone numbers')


    for numbers in list_of_Phone_numbers:
        for number in numbers:
            current_number = number
            for dict in list_of_dicts:
                while len(current_number) > 1:
                    if current_number in dict.keys():
                        print('phone number: {} Cost: {}'.format(number, dict[current_number]))
                        break
                    current_number = current_number[:-1]
if __name__ == '__main__':

    find_route_cost(['route-costs-106000.txt','route-costs-10.txt'], ['phone-numbers-1000.txt','phone-numbers-10.txt'])
