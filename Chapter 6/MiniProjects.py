# Mini Project – Countdown Timer (with 1-second gap) 

# Goal: 
# Print a countdown before something “exciting” happens (like “Launching...” or 
# “Happy New Year!”)


import time
count = int(input("Enter the counter time:-"))

print("\n Counter starts now!!")
for i in range(count , 0 , -1):
    print(i)
    time.sleep(1)

print("\n Happy New Year")