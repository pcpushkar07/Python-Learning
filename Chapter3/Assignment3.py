#Smart Temperature Converter

# Take input in Celcius and print its equivalent in Farenheit and Kelvin.
# (Use explicit type conversion and arithmetic operators.)

# Formula:

# ~ Fahrenheit = (C * 9/5) + 32
# ~ Kelvin = C + 273.15


C= float(input("What's the temperature:"))

F = (C * 9/5) + 32
K = C + 273.15

print("Converted value of Celcius into Farenhite" , F)
print("Converted value of Celcius into Kelvin" , K)


#Split Calculator

#Write a program that takes total bill amount and numbers of friends as input.
#Calculate how much each person will pay.
#Also print the data type of variable used.

# hint: (use float() and division operator)


bill = float(input("Enter the total bill amount here:"))
friends = int(input("Enter the number of Friends here:"))
split = (bill/friends)

print("Here's the final amount each person will pay" , split)