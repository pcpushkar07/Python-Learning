file = open("certificate.txt" , "r")
DataofFile = file.read()        
DataofFile= DataofFile.lower()

if "live" in DataofFile:
    print("Yes,it does contain the word 'live'")
else:
    print("NO")
