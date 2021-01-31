
# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze
# suma parametrilor care reprezintă numere întregi sau reale.



# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3)

def my_function(*args):
    sum = 0
    # Pt fiecare element
    #  Daca e numar
    #     adauga in suma
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)
    # for i in args:
    #     if type(i) == int or type(i) == float:
    #         print(i)

my_function(1,5,-3,"abc",[12,56,"cad"])



# ○ your_function() va returna 0.

def my_function(*args):
    sum = 0
    # Pt fiecare element
    #  Daca e numar
    #     adauga in suma
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)

my_function()


# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).


# intrebare - care e diferenta ditre linia 47 de cod- si 48?
# L47 definesti un singur keyword argument, la L48 poti primi un numar infinit de keyword arugments.

# def my_function(*args, param_1=0):
def my_function(*args, **kwargs):
    sum = 0
    # Pt fiecare element
    #  Daca e numar
    #     adauga in suma
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)

my_function(2,4,"abc",param_1=2)
# se traduce my function de! o apelezi asa nu pui egal.


# ● Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# # ○ suma tuturor numerelor de la [0, n]

def recursive_sum(n):
    if n == 0:
        return n
    return n + recursive_sum(n-1)

print(recursive_sum(5))



# ○ suma numerelor pare de la [0, n]
#

def recursive_sum_even(n):
    if n == 0:
        return 0
    if n%2 ==0:
        return n + recursive_sum_even(n-1)
    else:
        return recursive_sum_even (n-1)

print("this is recursive sum even\n")
print(recursive_sum_even(5))



# ○ suma numerelor impare de la [0. n]
def recursive_sum_uneven(n):
    if n == 0:
        return n
    # base case pentru ca functia sa se opreasca
    if n%2 !=0:
        return n + recursive_sum_uneven(n-1)
    else:
        return recursive_sum_uneven(n-1)

print("this is recursive sum uneven\n")
print(recursive_sum_uneven(9))




def recursive_sum(n):
    if n %2 !=0:
        return n
    return n + recursive_sum(n-1)

print(recursive_sum(5))



# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează 0



def my_function():
    user_inp = int(input("user input here: "))

    if type(user_inp) ==int:
        print (user_inp)
    else:
        return 0


print(my_function())



# valuue error o sa fie adaugata pe git dupa ce voi parcurge inregistrarea din clasa.


# schita
# 1
# 3
# 5
# nums = [1, 3, 5]
# sum = 0
# for i in nums:
#     sum = sum + i
# sum = 0
# sum += nums[0]
# sum += nums[1]
# sum += nums[2]
# print(sum)
# print(sum(my_function))

# def sum(a,b,c):
#     return a + b + c
# print (sum(5,6,7))

