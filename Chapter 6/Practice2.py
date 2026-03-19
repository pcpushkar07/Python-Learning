# 1.Write a program using for and range() to print all even numbers between 1 and 20.

# print("All even numbers between 1 and 20 are:-")

# for item in range(2 ,21 ,2):
#     print(item)


#2. Write a program to print numbers from 1 to 50, but print "Saumya Singh" 
# instead of numbers that are multiples of 5.

# for items in range(1 , 50 , 1):
#     if items%7==0: 
#         print("Pushkar")
#     if items%8==0:
#         print("Rushika")    
#     else:
#         print(items)

#3. write a program to print first 10 numbers divisible by 374

# n =1 
# i = 374
# while n<=10:
#     if i%374==0:
#         print(i)
#         i = i+374
#         n = n+ 1
#     else:
#         i+=1

# 4. Write a program to print the square of each number from 1 to 10 using a for loop.

# for num in range(1 ,11 ,1):
#     square = num**2
#     print(square)

# 11. Write a program that prints the multiplication table of any number entered by 
# the user using a for loop.     

# n = int(input("Enter your number"))

# for i in range(1 , 11 , 1):
#     print(f"{n} * {i} = {n * i}")


# 12 .Write a program that prints all numbers from 100 to 1 using for and range().

# for items in range(100 , 0 , -1):
#     print(items)

# 13. Saumya wants to print her username five times in uppercase letters. 
#  Write a program to print: 
 
# SAUMYA1SINGH   
# SAUMYA1SINGH   
# SAUMYA1SINGH   
# SAUMYA1SINGH   
# SAUMYA1SINGH 

# for items in range(1 , 6 , 1):
#     print("saumya1singh".upper())
    
# 14. You are given a list of Saumya’s favorite foods. Write a Python program to 
# print each food item using a for loop.

food = ["Samosa" , "Pav bhaji" , "Gulab Jamun" , "Rasgula"]

for food in range(1 , 5):
    print(food)