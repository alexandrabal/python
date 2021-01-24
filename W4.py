# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7,8,9,2,3,1,4,10,5,6]
# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_list.sort()
print(my_list)
# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
my_list.sort(reverse = True)
print(my_list)
# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
my_list.sort()
print(my_list[1::2])
# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
my_list.sort()
print(my_list[::2])
# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
print(my_list[2::3])
# a se păstra acuratețea indexilor - aceștia trebuie să fie cât mai specifici.
my_list = [7,8,9,2,3,1,4,10,5,6]
for i, e in enumerate(my_list):
    print(i,e)


