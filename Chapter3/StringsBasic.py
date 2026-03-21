# 1.Strings in Python:

# A string is a data type in Python that stores sequence of characters-letters, numbers, or symbols-enclosed in
# single('') , double(""), or triple(''' ''') quotes.quit
 
# examples:
# str1 = 'Hello'
# str2 = "Pushkar"
# str3 = '''Welcome to Python!'''

# -Note: Strings are immutable, meaning once created, thier content cannot be changed directly.

# ~Creating Strings:
# we know it already how to create a string.

# 2. String Concatenation:

# print("Hello" + "World")  output- Hello World

# -Lenght Of Syntax

# len("Pushkar") output: 7

# 3. INDEXING:

# Each character in a string has a position (index) starting from 0.

# str = "PushkarChaudhari"  

# Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# Chars: P U S H K A R C H A U D H A R I

# EX:

# str= "Samosa"
# print(str[0])       #S
# print(str[3])       #o

# Stings are immutable

# str[0] = 'B'   #ERROR: Strings cannot be changed directly.


# PRACTICE QUESTION

# Write a Python program that takes a user's name as input and prints:

# 1. The first character.
# 2. The last character.
# 3. The total length of the name.

str1= input("Enter your Name")
print("The name of the person is:" , str1)
length = len(str1)
print("The lenght of the name is:" , length)
print(str1[0])
print(str1[-1])

# 4. SLICING:

# Slicing lets you access a part of a string.

# Syntax:

# string[start : end]   #end index is excluded

# examples:

str = "GulabJamun"
print(str[0:5])  #Gulab
print(str[:6])   #GulabJ  (If starting index is left empty then it is called as 0 only)
print(str[5:])   #Jamun   (If last index is left empty then it automtically acquires length of the name)


# 5.Negative Indexing:

#   G  U  L  A  B  J  A  M  U  N
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

#PRACTICE QUESTION:

#Write a program that takes your favorite colour name as input and prints:
# - The middle 3 characters.
# - The last 2 characters.

color = input("Enter the color:")
mid = len(color)//2    #here // means the decimal part will be removed as suppose a word has 5 characters then the 5/2 will give you answer in decimal.
output1 = color[mid-1 : mid+2]
print(output1)
print(color[len(color)-2:])
 #    OR
output2= color[-2:]
print(output2)