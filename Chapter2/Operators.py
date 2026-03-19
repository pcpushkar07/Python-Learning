# OPERATORS IN PYTHON:

# Operators perform operations on variables and values.

#  TYPE                   EXAMPLE                                  DESCRIPTION

# Arithmetic            = - * / % **                      Math operations (** for power) (% for reminder)
# Comparison            == != > < >= <=                   Compare values, return True or False
# Logical               and or not                        Combine conditions
# Assingment            = += -= *= /=                     Assign or Modify values

x = 10 
y = 5 

print(x + y)
print(x - y)
print(x % y)
print(x/y)
print(x**y)
print(x*y)

#comparison operators:

print(x==y)    #Is the value pf x and y equal
print(x!=y)    #Is the value of x and y not equal
print(x>=y)    #Is x greater then or equal to y
print(x<=y)    #Is x less then or equal to y
print(x>y)     #IS x greater then y
print(x<y)     #Is x less then y

#Logical Operators:

print(x>y and x<y)    #And here says that ,I will print True if and only if both the statements on left and right of and are true.
print(x>y or x<y)     #Or here says that ,I will print True if any of the both statements is True.
print(not(x>y))       #NOT operator here just reverses the result as True will become false and false will become true.


#Assingment operator

a= 2
b = 3

a = a+6
a+=6

a=a-6
a-=6

a=a*8
a*=8

a=a/4
a/=4


#PRACTICE QUESTION: Write a program that takes two numbers and prints:

# - Their sum, difference and product.
# - Wether the first number is greater than the second.

c = 10
d = 20

print("Sum of two numbers is:" ,c+d)
print("Difference of two numbers is:" ,c-d)
print("Product of two numbers is:" ,c/d)

print("Is c greater then d" ,c>d)