# 5.Common string methods:

#  Method                           Description                                         Examples

# .upper()                Converts all characters to upper case               "Samosa".upper() --> 'SAMOSA'
# .lower()                Converts all characters to lower case               "Pushkar".lower() --> 'pushkar'
# .title()                Capitalizes the first letter of each word           "hello world".title() --> 'Hello World'
# .find()                 Returns index of first occurrence                   "banana".find("na") --> 2
# .replace(old,new)       Replaces all occurrences                            "Python is cool".replace("cool ,fun") --> 'Python is fun'
# .count(sub)             Counts occurrences                                  "mango".count("a") --> 1
# .endswitch(suffix)      Checks if string ends with given substring          "coder.".endswith(".") --> True
# .capitalize.()          Capitalizes first letter only                       "python".capitalize() --> 'Python'

#Just learn it and apply it as required.


#Write a program that:

# - Takes a sentence as input.
# - Converts it to lowercase.
# - Replaces all spaces " " with underscore.
# - Prints the new string.

str = "I Am Learning Python"
print(str.lower())
replace= (str.replace(" " , "_"))
print(replace)

