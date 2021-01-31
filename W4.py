# LISTS
# a list with the following elements 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (in this order)
my_list = [7,8,9,2,3,1,4,10,5,6]

# print a list in ascendent order
my_list.sort()
print("sorted " + str(my_list))


# print a list in a descendent order from the highest to the lowest
my_list.sort(reverse = True)
print(my_list)

# even numbers listed ascendently using slice (print only even numbers)
my_list.sort()
print(my_list[1::2])

# a list that contains uneven numbers (using the slice method)
my_list.sort()
print(my_list[::2])

# multiple of 3 using slice
print(my_list[2::3])

# print the index and element values of a list
my_list = [7,8,9,2,3,1,4,10,5,6]
for i, e in enumerate(my_list):
    print(i,e)


