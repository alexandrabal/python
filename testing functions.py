# my_list = [5,2,3]
# list_length=len(my_list)
# index = 0
# #
# # while index < list_length:
# #     list_element = my_list[index]
# # #     print(f" element (list_element) from position [index] is even number)
# #     index += 1
# #
# # for i in my_list:
# #     print (i)
#
# for e in enumerate(my_list):
#     print(e[0])

# # print("index", index)
#
# for index in range(len(my_list)):
#     print (index, my_list[index])
#
# for index, elem in enumerate(my_list):
#     print (index, elem)
#
# index = 0
# for i in my_list:
#     print(index, i)
#     index += 1
# # for index in range(len(my_list)):
# #     print(index, my_list[index], end = "\n")
#
#
# def my_sum(a,b):
#     return a + b
# print(my_sum(5,2))
#
# def view_comparison (a,b):
#     return a < b
# print(view_comparison)
#
#
# def multiply_funciton(a,b):
#     return a * b
# print(multiply_funciton)
#
# my_num = 790
# my_budget = 25
# print(my_sum(my_num,my_budget))
#
# print(view_comparison(my_num,my_budget))
#
# my_number_of_days = 15
# campaign_budget = 2
# print(multiply_funciton(my_number_of_days,campaign_budget))
#
#
# my_total_campaign_budget = campaign_budget* my_number_of_days
# december_month =3
#
# print(multiply_funciton(december_month,my_total_campaign_budget))
#

#
# my_list.sort(key=rank, reverse =True)
# print(my_list)
#
#
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
#

#
# my_list = [{"first_name":"John",
#             "rank":3},
#             {"first_name": "Kevin",
#              "rank": 5}]
#
# def rank(user):
#     return user["rank"]
#
# my_list.sort(key=rank)
# print(my_list)
#
#
# my_list = [{"first_name":"John",
#             "rank":3},
#             {"first_name": "Kevin",
#              "rank": 5}]
#
# my_sorted_list = sorted(my_list, key=lambda user:user['rank'])
# # lambda most of the time returns
# print(my_sorted_list)

import copy

player =[{"first_name":"John",
            "rank":3},
            {"first_name": "Kevin",
             "rank": 5}]

def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player["is top 3"] = True if updated_player ["rank"] <= 3 else False
    return updated_player

players_with_top_3_value = map(lambda u: u["first_name"], player)
print("players_with_top_3_value =", list(players_with_top_3_value))

print(type(players_with_top_3_value))



