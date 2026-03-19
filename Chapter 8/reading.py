# Reading Files:

# a) Read entire file:(f.readline())

# with open("report.txt" , "r") as f:
#     data = f.read()
#     print(data)

# b) Read line by line:

# with open("report.txt" , "r") as f:
#     line = f.readline()
#     print(line)

# EX-

with open(r"F:\Python code\Chapter 8\newtextfile.txt" , "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    print("line 1:" , line1)
    print("line 2:" , line2)
    print("line 3:" , line3)
    print("line 4:" , line4)

# c) Read all lines:(f.readlines()) - It gives list of all the lines as string.

# with open(r"F:\Python code\Chapter 8\newtextfile.txt" , "r") as f:
#     line = f.readlines()
#     print(line)

# Q-Print how many lines are present in notes.txt.

with open(r"F:\Python code\Chapter 8\notes.txt" , "r") as f:
    lines = f.readlines()
    print(lines)
    print("Lenght of the lines is:" , len(lines))

# Append Mode:

#Adds new Content:

with open(r"F:\Python code\Chapter 8\notes.txt" , "a") as f:
    f.write("Hello!!")



# AUTOMATING FILE TASKS(Copy,Rename , Delete)

# Using Python Module:

# Think of a Module as ToolBox.

# Each modules gives you tools(functions) which you dont have to write again.

# COPY FILE:

# import shutil                                  # shutil is a module to copy files.
# shutil.copy("demo.txt" , "backup_demo.txt")

#Rename File:

# import os
# os.rename("demo.txt" , "new_demo.txt")

# DELETE FILE:

# import os
# os.remove("oldfile.txt")



