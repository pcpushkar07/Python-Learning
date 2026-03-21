# 3⃣ Tuples in Python:-

# Definition-

# - A tuple is a built-in data type that stores multiple values like a list, but it is immutable (cannot be changed after creation). 
# - Difference in list and tuple is that , Tuples use ( ) instead of [ ]   
# - Also list is mutable and tuple is immutable.

# tup = (87, 64, 33, 95, 76) 
# print(tup[0])    # 87 

# Tuple Examples 

t1 = ()                            # Empty tuple   
print(t1)    
t2 = (1,)                          # Single element tuple (comma required)      
print(t2)
t3 = ("Samosa", "Pizza", "Burger") 

# Immutable Nature 
# tup = (10, 20, 30) 
# tup[0] = 100             # ❌ Error - cannot modify tuples

# Tuple Methods

# Method                     Description                             Examples

# .count(el)              Countes occcurance of the values       tup.count(10)
# .index(el)             Returns first index of element         tup.index(30)
 