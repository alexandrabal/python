# a function with undefined number of parameters and calculate the sum of integer or float numbers.
# test case (1, 5, -3, ‘abc’, [12, 56, ‘cad’]) to return  3 (1 + 5 - 3)
# (for every element if it's a number to be added in +1

def sum_of_real_numbers(*args):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)

sum_of_real_numbers(1,5,-3,"abc",[12,56,"cad"])


# ○ your_function() which returns 0.
def test_empty_parameters(*args):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)

test_empty_parameters()

# ○ your_function(2, 4, ‘abc’, param_1=2) which returns 6 (2 + 4).

def sum_of_first_two(*args, **kwargs):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    print(sum)


sum_of_first_two(2,4,"abc",param_1=2)


# a recursive function with integer numbers as parameters - calculates sum of numbers from [0 to n]

def recursive_sum_of_integers(n):
    if n == 0:
        return n
    return n + recursive_sum(n-1)

print(recursive_sum_of_integers(5))



# recursive function of sum of even numbers [0, n]
def recursive_sum_even(n):
    if n == 0:
        return 0
    if n%2 ==0:
        return n + recursive_sum_even(n-1)
    else:
        return recursive_sum_even (n-1)

print("this is recursive sum even\n")
print(recursive_sum_even(5))



# a recursive function that calculates the sum of uneven numbers [0. n]
def recursive_sum_uneven(n):
    if n == 0:
        return n
    # base case for the function to stop
    if n%2 !=0:
        return n + recursive_sum_uneven(n-1)
    else:
        return recursive_sum_uneven(n-1)

print("this is recursive sum uneven\n")
print(recursive_sum_uneven(9))


# a function that gets user input and returns an integer.
# if the number is not an integer returns 0

def get_user_input():
    user_inp = int(input("user input here: "))

    if type(user_inp) ==int:
        print (user_inp)
    else:
        return 0

print(my_function())

# valuue error to be added in get_user_input
