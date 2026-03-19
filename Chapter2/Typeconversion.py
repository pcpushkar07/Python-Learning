# TYPE CONVERSION:

# ~Type conversion means changing one data type to another.

# a. IMPLICIT CONVERSION(Automatic)

# Python automatically coverts smaller data types to larger ones to prevent data loss.

# ex:

# x = 5 #int
# y = 2.5 #float
# z= x= y #python converts int--->float
# print(z)  #7.5


# b. EXPLICIT CONVERSION (Manual)

# Manually converts data types using built-in functions:

# x= "10"
# y = int(x)    #str--->int
# print(y + 5)  #output: 15

# Common functions : int(), float(),str(),bool()

#PRACTICE QUESTION: Take a number as input, convert it to a float, and print both the orignal and converted value with thier data types.

a = input("Enter your number:")
print("Your orignal number is:", a)
print(type(a))
b = float(a)
print("Converted number is:" , b)
print(type(b))