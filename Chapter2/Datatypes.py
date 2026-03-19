#DATA TYPES IN PYTHON:

# Python has several built-in data types. They define the type of value a variable holds.

# TYPE                             EXAMPLE                                  DESCRIPTION

# int                            x=10                                     Whole numbers(+ve or -ve)
# float                          y=3.14                                   Numbers with decimals
# str                            name= "string"                           Sequence of characters
# bool                           flag= True                               Logical values: True or False

# Note: Use type() function to check the variables data type.

food = "Dosa"        #string
age = 25             #int
area = 34.5          #float
name = "Pushkar"     #string
print("Data type variable name is", type(name))
print(type(area)) 
print(type(age))
print(type(food))

# question 1: Program to take age as input and print value entered and its data type

age = int(input("Enter the age of person here:"))
print("The age of the person is:" , age)
print("Data type is", type(age))

