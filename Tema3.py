# create a csv with data
# read data from a csv
# output folder json

import csv
import copy
import json

''' Read cars from input'''

csv_file = open ("input.csv","r")
rows = csv.reader(csv_file, delimiter ="\t")
for row in rows:
    print(row)
my_data = list(csv.reader(csv_file))
csv_file.close()
print(my_data)

'''Append each row of the dictionary to cars '''
# print(my_data)
# Don't include the header which is the column names in an xls. use slice
skip_header = my_data[1:]
cars=[]

for row in skip_header:
    # print (row)
    my_cars_dictionary = {
        "brand":row[0],
        "model":row[1],
        "price":int(row[2]),
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
        print (updated_car)
    if car["hp"] > 180:
        updated_car["power_category"] = "sport car"

    # slow_car["is a slow car"] = True if slow_car ["hp"] < 120 else False
    return updated_car

my_cars_dictionary= list(map(check_hp,cars))
print(my_cars_dictionary)

# my_new_cars_dictionary = [{key: value for key, value in zip(header, element)} for element in my_cars_dictionary]
# print(my_new_cars_dictionary)

with open('my_output.json', 'w') as json_file:
    json_object = json.dumps(my_cars_dictionary)
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
def filter_for_speed(car):
    if car["power_category"] == "slow car":
        return True
    else:
        return False

slow_cars = filter(lambda car: car["power_category"] == "slow car", my_cars_dictionary)
print(type(slow_cars))
# print(list(slow_cars))
slow_cars_list = list(slow_cars)

fast_cars = filter(lambda car: car["power_category"] == "fast car", my_cars_dictionary)
# print(list(fast_cars))
fast_cars_list = list(fast_cars)

sport_cars = filter(lambda car: car["power_category"] == "sport car", my_cars_dictionary)
# print(list(sport_cars))
sport_cars_list = list(sport_cars)

# print(type(json.object),json_object)
# json_file.write(json_object)

with open("slow_cars.json","w") as my_slowcars_file:
    json_slowcars_object = json.dumps(slow_cars_list)
    my_slowcars_file.write(json_slowcars_object)

with open("fast_cars.json","w") as my_fastcars_file:
    json_fastcars_object = json.dumps(fast_cars_list)
    my_fastcars_file.write(json_fastcars_object)

with open("sport_cars.json","w") as my_sportcars_file:
    json_sportcars_object = json.dumps(sport_cars_list)
    my_sportcars_file.write(json_sportcars_object)




