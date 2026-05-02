# # 7. OOP Concepts - Abstraction & Enscapsulation:
 

# There are 4 pillers of oops:

# 1.Abstraction
# 2.Enscapsulation
# 3.Inheritance
# 4.Polymorphism


# 1.ABSTRACTION:

# Showing only essential deatils and hiding internal complexity.

# ex- You use Instagram without knowing its backend code.

# In Python:

# class Payment:
#     def pay(self)
#         print("Payment Successful")


# 2. Enscapsulation:

# Wrapping Data + Methods inside a single unit(class).
# Data is protected using private variables.

# ex- 

# class Account:
#     def __init__(self , bal):
#         self.__balance = bal    #private

#     def show_balance(self):
#         print("Balance:" , self.__balance)    
        
# 3.Inheritance:


# MEANING:

# When one class(child) gets the properties and methods of another class(parent).
# It avoids repeating code.

# THINK:

# Child class uses everything which parent class has:

# FULL CODE:

#parent class

class vehicle:
    def start(self):
        print("Vehicle is Starting")

# child class 1

class car(vehicle):
    def drive(self):
        print("Car is now starting")

# child class 2

class Bike(vehicle):
    def ride(self):
        print("Bike is now riding")

# child class 3

class Truck(vehicle):
    def load(self):
        print("Truck is loading goods")

# Using the classes:


c = Car()
c.start()  #from parent
c.drive()  # child specific


b = Bike()
b.start()   # from parent
b.ride()    # child specific

t = Truck()
t.start()    # from parent
t.load()     # from child 


#Polymorphism

# Meaning:

# Same function name, but different behaviour in different classes.


# One fucnction name--> many different behaviours depending on the objects calling it.

# THINK:
# Different objects respond in thier own unique way.

# If I say"sound",

# -A dog will bark.
# - A cat will meow.
# - A cow will moooo

# same word--different actions.
# this is polymorphism.

# Full Code:

# Ex-1: Animal Sound:

class Dog:
    def sound(self):
        print("Dog says: Bark")

class cat:
    def sound(self):
        print("Cat says :meow")        

class cow:
    def sound(self):
        print("cow says :moo")        

# Polymorphism in Action;

animals = [Dog(), Cat() , Cow()]

for a in animals:
    a.sound()    # same function name, different output

# SIMPLE WAY TO REMEMBER:

# "Same name , different action"
# - same method name
# - diffrent output
# - depends on the object