# create a csv with data
# read data from a csv
# output folder json

import csv
import copy
import json

# Read cars from input
csv_file = open ("input.csv","r")
    # rows = csv.reader(csv_file, delimiter ="\t")
    # for row in rows:
    #     print(row)
my_data = list(csv.reader(csv_file))
csv_file.close()

# Each row from a dictionary, append to cars
# print(my_data)
# don't include the header which is the column names in an xls. use slice

skip_header = my_data[1:]
cars=[]
for row in skip_header:
    # print (row)
    my_cars_dictionary = {
        "brand":row[0],
        "model":row[1],
        "price":row[2],
        "hp":int(row[3])}
    cars.append(my_cars_dictionary)
print(cars)

# Map - for each car set new key "power_category" slow_cars / fast_cars / sports_cars

def check_hp(car):
    updated_car = copy.deepcopy(car)
    if car["hp"] < 120:
        updated_car["power_category"] = "slow car"
    if car["hp"] >= 120 and car["hp"] < 180:
        updated_car["power_category"] = "fast car"
    if car["hp"] > 180:
        updated_car["power_category"] = "sport car"

    # slow_car["is a slow car"] = True if slow_car ["hp"] < 120 else False
    return updated_car

my_cars_dictionary= list(map(check_hp,cars))
print(my_cars_dictionary)

my_new_cars_dictionary = [{key: value for key, value in zip(header, element)} for element in my_cars_dictionary]
print(my_new_cars_dictionary)
with open('my_output.json', 'w') as json_file:
json_object = json.dumps(my_new_cars_dictionary)
json_file.write(json_object)


# Map - for each car set new key "price_category" cheap / medium / expensive
for car in my_cars_dictionary:
     if car["power_category"] == "slow car":
         print(car)
     if car["power_category"] == "fast car":
         print(car)
     if car["power_category"] == "sport car":
         print(car)

# # filter - filter only fast cars
# def filter_for_speed(car):
#     if car["power_category"] == "slow car":
#         return True
#
# all_cars = filter(my_cars_dictionary,car)
# new_all_cars = list(all_cars)
# print(type(new_all_cars))


# print(type(json.object),json_object)
# json_file.write(json_object)

# with open("output_data/slow_cars.json","w") as my_output_file:
#     my_output_file.write("text")
#     print(my_output_file)

# my_slow_cars = filter(check_hp, lambda "sport car" in car: car)
# print(type(my_slow_cars))
# print(my_slow_cars)


# my_cars = []
# with open ("input.csv") as csv_file:
#     header = ()
#     cars_data = []
#     for index,line in enumerate(csv_file.readlines()):
#         if index == 0:
#             header = line.split(",")
#         else:
#             cars_data = line.split(",")
#     print("cars_data", cars_data)
#
# my_sorted_cars = sorted(my_cars, key=lambda a: a.get('hp', 0), reverse=True)
# print(my_sorted_cars)
#
# def view_numbers_comparison(a, b):
#         print(f'{a} < {b} results in {a < b}')

    # print("header", header)
    # print("cars_data", cars_data)

# slow_cars = sorted(list_of_cars, key= lambda c: c ["hp"])
# print(slow_cars)


# my_slow_cars = list(my_slow_cars)
# print(my_slow_cars)