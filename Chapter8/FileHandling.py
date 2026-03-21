#FILE HANDLING:

#File handling allows Python Program to store, read, and manage data saved on computer - such as notes , logs , students record , or CSV files.

#TYPES OF FILES:

# There are two types of files:

# 1. Text Files: Human readable content.

# ex- .txt , .csv , .log

# 2. Binary files :Data stored in encoded form.

# ex - .png , .jpg , .mp4 , .pdf , .exe

# OPENING FILE:
 
# Python uses the open() function:

# file = open("file name" , "mode")

# MODE                      MEANING

# "r"            -         read(default)
# "w"            -        write(overwrite file)
# "a"            -         append(adds at end)
# "x"            -         Create new file;error if exits
# "t"            -         Text mode
# "b"            -         Binary mode

# ex - 

# f= open("notes.txt" , "r")
# print(f.read())

# f= open("notes.txt" , "r")              #file is opened here. 
# data = file.read()                      #Data of the file is stored here.

# print("Data of file is:" , data)

# Practice Questions:

#Q.1 - Write a program to read a text from a given file certificate.txt and find whether it contains the word live.

# file = open(r"F:\Python code\Chapter 8\certificate.txt" , "r"/)
file = open("certificate.txt", "r")
DataofFile = file.read()        
DataofFile= DataofFile.lower()

if "live" in DataofFile:
    print("Yes,it does contain the word 'live'")
else:
    print("NO")

#Q.2- Open a file report.txt in write mode.

# file = open("report.txt" , "w")
# fileData = file.write(HELLO!!)



 # USING WITH STATEMENT:

# This is the recommended method which automatically closes the files.
# -No need to use close method.