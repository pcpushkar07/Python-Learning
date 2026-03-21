# Assingment question:

# 1. Ask the user for their 3 favorite movies and store them in a list.
     
# 2. Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().
 
# 3. Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

movie1 = input("Enter your first movie name")
movie2 = input("Enter your second movie name")
movie3 = input("Enter your third movie name")

movielist = [movie1 , movie2 , movie3]
print(movielist)


marks = [87 , 64 , 33 , 95 , 76]
print(marks)
print(max(marks))
print(min(marks))

marks1 = int(input("Enter your marks here:-"))
if(marks1 >= 90):
    print("A GRADE")
elif(marks1 >= 80 ):
    print("B Grade")    
elif(marks1 >= 70):
    print("C grade")
else:
    print("D Grade")