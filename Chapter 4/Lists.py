# 2⃣ Lists in Python:
#  
# Definition 
# -A list is a built-in data type that can store multiple values in a single variable.Lists are mutable (can be changed) and can  store different data types. 
# -Stored in square brackets.
 
# Example: 
 
# marks = [87, 64, 33, 95, 76] 
# student = ["Saumya Singh", 21, "Delhi"] 


# Accessing Elements (Indexing)-

# Each item in a list has an index starting from 0. 

# foods = ["Samosa", "Pizza", "Burger"]
# print(foods[0])     # Samosa  
# print(foods[2])      # Burger

foods = ["Samosa", "Pizza", "Burger", "Pasta", "Ras Malai"] 
print(len(foods))      #length of the varaible or list
print(foods[1])        #Indexing of variable

# Modifying Elements-

# Lists are changeable. 

# foods[0] = "GulabJamun" 
# print(foods)   # ['GulabJamun', 'Pizza', 'Burger'] 

# List Slicing 

# You can extract parts of a list using slicing. 

# marks = [87, 64, 33, 95, 76] 
# print(marks[1:4])             # [64, 33, 95]
# print(marks[:3])              # [87, 64, 33] 
# print(marks[-3:-1])           # [33, 95] 

# List Functions:-

# Function              # Description                       # Example 
                            
# len(list)         Returns length  of list              len(marks) → 5
 
# max(list)         Returns largest value                max(marks) → 95

# min(list)         Returns smallest value               min(marks) → 33


marks = [99 , 100 , 95 , 80]
print("Length of the List is:-",len(marks))
marks[1] = 98
print("Changed List:-",marks)   #This shows List is mutable ,its value can be changed.
print("Maximun marks in this list is:-",max(marks))
print("Minimum value in this list is:-" , min(marks))


# Common List Methods 

#  Method                    Discription                        Example

# .append(el)             Adds element at the end             marks.append(99)

# .insert(i,el)           Inserts element at index            marks.insert(1,80)

# .remove(el)             Removes first occurance             marks.remove(64) 

# .pop(i)                 Removes element at index            marks.pop(2)

# .sort()                 Sorts list in acending order        marks.sort() 

# .reverse()              Reverses the list                   marks.reverse()                         
                    
              
marks = [99 , 100 , 95 , 80]

marks.append(90)
print(marks)
marks.insert(1 , 93)
print(marks)
marks.remove(100)
print(marks)
marks.pop(3)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)

#PRACTICE QUESTION 2:

# Write a program that takes names of 3 favorite foods from the user and stores 
# them in a list. Then print the list and its length.

food1 = input("Enter your food 1:-")
food2 = input("Enter food 2:-")
food3 = input("Enter food 3:-")

foodlist = [food1 , food2 , food3]
print(foodlist)
print(len(foodlist))