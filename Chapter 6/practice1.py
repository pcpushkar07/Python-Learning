# # PRACTICE QUESTION:-

# # 1. Write a Python program to print numbers from 1 to 10 using a while loop.

# num = 1 
# while num<=10:
#     print(num)
#     num += 1 

# # 2.  Write a program to print numbers from 10 down to 1 using a while loop.
# print("Solution to Problem 2:-")

# num1 = 10 

# while num1>=1:
#     print(num1)
#     num1 = num1-1

# # 3. Write a program to print all even numbers between 1 and 50 using a while loop.
   
# print("Solution to problem 3")

# num2 = 1

# while num2<=50:
#     if num2%2==0:
#         print("Even numbers",num2)
#     elif num2%2!=0:
#         print("Odd numbers",num2)
#     num2 =num2+1    

# 4. Write a program that prints the sum of first n natural numbers. 
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.


# n = int(input("Enter a number:-"))
# sum = 0
# while n>=1:
#     sum = sum + n
#     n = n-1
    
# print("Sum=", sum)
# print("Last value of n=" , n )


    
# 5. Write a program to print this pattern using a while loop: 

# * 
# * * 
# * * * 
# * * * * 


# n=1 

# while n<=4:
#     print("*" * n)
#     n = n+1

# 6. Saumya wants to print her name 5 times, but each time with a number in 
# front of it. Write a program using a while loop that prints:

# 1. Saumya Singh   
# 2. Saumya Singh   
# 3. Saumya Singh   
# 4. Saumya Singh   
# 5. Saumya Singh 

# n = 1

# while n<=5:
#     print(n , "Saumya Singh")
#     n = n+1+

# 7.  Write a program to print the multiplication table of any number using a while loop.

a = int(input("Enter the Value="))
n = 1

while n<=10:
    print(f"{a} * {n} = {a * n}")
    n=n+1

 