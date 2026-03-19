#1. CONDITIONAL STATEMENTS IN PYTHON:

# Conditional statements allow your program to make decisions - run different parts of code based on certain conditions. 

# ~What Are Conditions? 
# A condition is simply a statement that can be either True or False. 

# Example: 

# age = 18 
# print(age >= 18)   # True 


# ~if Statement: 

# Used to run a block of code only when the condition is True. 

# age = int(input("Enter your age: ")) 
# if age >= 18: 
#   print("You are eligible to vote.") 

# If the condition is false, nothing happens. 

# Note : If we want to add something under the statements, then 1 tab space(intendation) is mendatory.

# ~if-else Statement:

# marks = int(input("Enter your marks: ")) 
# if marks >= 40: 
# print("You passed!") 
# else: 
# print("You failed!") 

# if-elif-else Statement 
#      Used when we have multiple conditions. 

# marks = int(input("Enter marks: ")) 
# if marks >= 90: 
# print("Grade A") 
# elif marks >= 80: 
# print("Grade B") 
# elif marks >= 70: 
# print("Grade C") 
# else: 
# print("Grade D") 

# ex-1
marks = int(input("Enter your Marks here:"))
if(marks >= 90):
    print("Your Grade is A")
elif(marks >= 80):
    print("Your Grade is B")
elif(marks >= 65):
    print("Your GRade is C")
else:
    print("Your Grade is D")   


#ex-2
age = int(input("Your age:"))
if(age >= 18):
    print("You are eligible to Vote")
else:
    print("You are not eligible to Vote")

# Practice Question 1 

# Write a Python program that takes a number as input and prints: 
# ● “Positive” if number > 0 
# ● “Zero” if number == 0 
# ● “Negative” if number < 0

num = float(input("Your Number-"))

if(num > 0):
    print("Positive")
elif(num == 0):
    print("Zero")
elif(num < 0):          # WE CAN USE elif or else here ,both are correct.
    print("Negative")
