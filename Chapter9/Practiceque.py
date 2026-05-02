# Create class student that takes 3 marks and has a method average()

class student():
    def __init__(self , name , listOFMarks):
        self.name = name
        self.listOFMarks = listOFMarks
        
    def average(self):
        sum = 0
        for eachValue in self.listOFMarks:
            sum = sum + eachValue

        average = sum/3
        print("Average of Marks is-" , average) 


student1 = student("Pushkar" , [98,99,95])
student1.average()      

# Create static method to validate if a number is even.

