import numpy as np
from pprint import pprint

def build_car_list():
    car_list = []
    with open('files/input.txt', 'r') as input_file:
        car_data = [line.strip().split(', ') for line in input_file.readlines()[1:]]
        car_data = [{'id': int(car[0]), 'miles': float(car[1]), 'model': ''} for car in car_data]

    with open('files/car-ids.txt', 'r') as id_file:
        valid_ids = {int(line.split(', ')[0]): line.split(', ')[1].strip() for line in id_file}

    car_array = np.array(car_data)

    filtered = list(filter(lambda car: car['miles'] >= 10000, car_array))

    for car in filtered:
        object = {'id': car['id'], 'miles': int(car['miles']), 'model': valid_ids[car['id']]}
        car_list.append(object)
        
    return car_list

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()