# OOPS (Object Oriented Programming) in Python:

# OOPS helps us structure programs using real world concepts like objects,classes,attributes and behaviours.
# Instead of writing everything in one place,we organizw code into one place,we organizwe code into objects- just like real-life entities.

# Ex- student ,Car ,bank account, mobile phone each can be represented as object in Python.

# 1. What is OOPS?

# OOP is a programming style where we use:

# - class - Blueprint
# - Object - Real isinstance
# - Attributes - Data
# - Methods - Behaviours (functions inside classes)

# Using OOP makes code:

# - Reusable
# - Organized
# - Easy to Maintain
# - Similar to real-world objects

# 2. Class and Object:

# Class: A blueprint/template

# Object: A real entity created from the class
    
# ex:

class Vehicle:
    color="Black"                #variables in class are called "attributes"
    model="Fortuner"
    price="51 lakh"

# Object Creation:

car=Vehicle()
print(car.color)

bike=Vehicle()
print(bike.color)

aeroplane=Vehicle()
print(aeroplane.model)
print(aeroplane.color)


# We created one class and three objects of that class.


# Q- Create a class Laptop with attributes: brand, RAM , price. Create two object with with different values.

class Laptop:
    brand = "HP"
    RAM = "16 GB"
    price = "97k"

Laptop1 = Laptop()
Laptop1.brand = "MacBook"
Laptop1.RAM = "16 GB"
print("Laptop1 Brand" , Laptop1.brand)
print("Laptop1 RAM" , Laptop1.RAM)
print("Laptop1 Price" , Laptop1.price)

Laptop2 = Laptop()
Laptop2.brand = "Lenovo"
print("Laptop2 Brand" , Laptop2.brand)
print("Laptop2 RAM" ,Laptop2.RAM)
print("Laptop2 Price" , Laptop2.price)

# Note: The weightage of an attribute in object is more then in class so it can pleace class attributes easily.

# 3. Instance Attribtes vs Class Attributes:

# ---Class Attributes:

# Shared by all objects

# ex-    class student:
#             college = "XYZ Institute"

# Instance Attributes:

# Unique for each object.

        













