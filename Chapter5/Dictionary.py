# 1⃣ Dictionary in Python

# Definition 

# -A dictionary is a built-in data type in Python used to store data in key–value pairs.  

# -Each key is unique and maps to a value. 

# -Dictionaries are unordered, mutable (changeable), and don’t allow duplicate keys.

# Indexing is not allowed in Dictionary.

# Example: 

# student = { 
# "name": "Saumya Singh", 
# "age": 25, 
# "city": "Sultanpur" 
# } 

# Here: 

# ● "name", "age", "city" → keys 
# ● "Saumya Singh", 21, "Delhi" → values

# Accessing Values:-

# You can access a value using its key: 

# print(student["name"])     # Saumya Singh 
# print(student["city"])     # Delhi


# Adding or Updating Values:- 

# You can add new key-value pairs or modify existing ones: 

# student["college"] = "ABC University"         # adds new key-value
# student["age"] = 22                           # update existing value
# print(student)

# Removing Items:-

# student.pop("city")     #removes key 'city' 
# print(student)


# Dictionary methods:-

#  Method                         Description                                  Examples

# .keys()                    Returns all Keys                                 student.keys()

# .values()                  Returns all values                               student.values()

# .items()                   Returns all key-value pairs as tuples            students.items()
    
# .get(key)                  Returns value of a key safely                    student.get("name")

# .update(new_dict)          Updates dictionary with another                  student.update({"city" : "Lucknow"})


# Nested Dictionary:

# You can store another dictionary inside a dictionary. 

# Example: 

# profile = { 
# "username": "saumya1singh", 
# "details": { 
# "followers": 1200, 
# "verified": True 
# } 
# }

# print(profile["details"]["followers"])   # 1200 


# Practice Question 1:

# Create a dictionary named marks to store marks of 3 subjects. Add the subjects one by one and print the final dictionary.

marks = {
    "Maths" : 99,
    "Science" : 98,
    "English" : 95
}

print(marks)

    #   or

marks2 = {}

marks2["Maths"] = 99
marks2["Science"] = 96
marks2["Computer Science"] = 91

print(marks2)