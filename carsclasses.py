import csv

csv_file = open ("input.csv","r")
rows = csv.reader(csv_file, delimiter ="\t")

my_data = list(csv.reader(csv_file))
csv_file.close()
print(my_data)

class Car:

    def __init__(self, brand, model, price, hp):
        self.brand = brand
        self. model = model
        self. price = price
        self. hp = hp

car1_from_list = my_data[2]
car1 = Car(car1_from_list[0], car1_from_list[1], car1_from_list[2], car1_from_list[3])
print(car1)
print(car1.price, car1.brand)