# 2⃣ Sets in Python 

set1 = {"Pushkar" , 97 , "Raver" , 30 , 50}
print(set)

#empty set:

empty_set = {}

      #OR 
# empty = set()      

student = {"Pushkar" , 10 , "Maths" , 30 , 50}

student.add("OBC")                        #adding an element.
print(student)
student.remove(10)                        #removing an element
print(student)
student.pop()                             #removing random element
print(student)

print(student.union(set1))                #union of two sets.
print(student.intersection(set1))         #intersection of sets.

#Problem solving:

# You are given a list of programming languages: 
# ["Python", "Java", "C++", "Python", "Java", "C"] 
# Convert it into a set and print how many unique languages Divya knows.


programmingList = ["Python", "Java", "C++", "Python", "Java", "C"] 

programmingSet = set(programmingList)
print(programmingSet)
print("These are the number of languages Divya knows :-" , len(programmingSet))

