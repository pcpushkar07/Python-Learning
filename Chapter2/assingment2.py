# Assingment question 2: Take diameter as input and calculate the area of a circle.

diameter = int(input("Enter the value of Diameter:"))  #int is used to make the string as integer,because we can't perform the divide operation on string.
radius = diameter/2
print("Radius of the circle is:" , radius )
area = 3.14 * (radius ** 2)
print("Area of Circle is:" , area)

age = int(input("Enter the age of person here:"))
print("The age of the person is:" , age)
print("Data type is", type(age))