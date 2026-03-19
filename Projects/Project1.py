# Mini Project – Expense Tracker_____


print(" :Welcome to Expense Tracker:")


expenseList = []     #Expenses will be stored in form of dictionary

while True:
    print("===MENU====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View total Expense")
    print("4. Exit")

    choice = int(input("Please Enter your Choice ->"))

#ADD EXPENSE:
   
    if choice==1:
        date = input("Enter the Date :")
        category = input("Enter the Category (Food , Travel , Grocery , Shopping) :")
        description = input("Detail about your expenses :")
        amount = float(input("Enter the total amount of expenditure :"))

        expense = {
            "date"  : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenseList.append(expense) 
        print("\n Expense added succesfully !!!")

#View all expenses: 

    elif choice==2:
        if len(expenseList == 0):
            print("ADD YOUR EXPENSES FIRST...")
        else:
            count = 1
            for eachexpense in expenseList:
                print(f"Expense No. {count} ->" ,{eachexpense["date"]} , {eachexpense["category"]} , {eachexpense["description"]} , {eachexpense["amount"]})
                count+=1


# Final Amount:

    elif choice==3:
        total==0
        for eachexpenses in expenseList:
            total = total + eachexpenses["amount"]
            
        print(" \n Your total expense is :-", total) 


#EXIT:

    elif choice==4:
        print("Thank for using our system !")
        break

    else:
        print("INVALID CHOICE. Choose right one")   