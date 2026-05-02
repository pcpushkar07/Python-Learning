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


# Q- Create a class Laptop with attributes: brand, RAM , price. Create two objects with different values.

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

# class student:
#     college = "XYZ Institute"
#     def __init__(self,name):
#         self.name = name

# s1 = student("saumya")
# s2 = student("Aman")        



class student:
    schoolname = "ABC SChool"

    def __init__(self):
        print("whenever a new object is created ,I am called automatically")
        print(self)

student1= student()
print("Student 1" , student1)

student2 = student()
print(student2)

        

# 4. The __init__() Constructor:

# The __init__() function runs automatically whenever an object is created. It is used to initialize attributes.

# Example:


class Student():
    schoolName ="ABC School"

    def __init__(self , name , course):
        self.name =name
        self.course = course

student1 = Student("Khushi" , "Btech")      #init method will be called
print("student1 name-" , student1.name)
print("student1 course-" , student1.course)

student2 = Student("Ankit" , "Bsc")
print("student2 name-" , student2.name)
print("student2 course-" , student2.course)
        

# 5. Methods (FUnctions inside Class):

# Methods define what a object can do.

# Example- 

# class student:
#     def __init__(self , name):
#         self.name =name

#         def hello(self):
#             print("Hello" , self.name)

# s1 = student("Pushkar")
# s1.hello()


# 6. Static Methods:

# Static methods do no use self.
# They are used for utility-level function.


# ex- 

# class student():
#     @staticmethod
#     def school():
#         print("ABC Public School")     #generic name


















