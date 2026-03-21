#Function defination with Parameters.
def average(a=10 , b=20):
    averageValue = (a+b)/2
    print(averageValue)

#Function calling with Argument.

average(5 ,10)
average(7 ,10)
average(80 ,98)
average(2 ,4)
average()             #IF we dont want to pass any arguments then we give some default values as parameters...To not give error...

# PRACTICE QUESTION:-

# 1.Write a function show_age(name, age) that prints: "Saumya Singh is 21 years old."

def show_age(name, age):
    print(f"{name} is {age} years old.")


show_age("Saumya Singh", 10)

# 2.  Create a function add_numbers(a, b) that prints both the sum and difference.


def add_numbers(a, b):
    sum= a + b
    diff = a - b
    print("sum=" ,sum)
    print("diff=" ,diff)

add_numbers(2 , 1)


# 3.  Write a function fav_food(food) that prints "Saumya loves <food>".

def fav_food(food):
    print(f"Saumya loves {food}")

fav_food("pani puri")

