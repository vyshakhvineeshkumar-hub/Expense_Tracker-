# Expense Tracker
expenses=[]
def add_expense():
    date=input("Enter date (DD-MM-YYYY):")
    category=input("Enter category(Food,Travel,etc):")
    amount=float(input("Enter amount(₹):"))

    expenses.append({
        "date":date,
        "category":category,
        "amount":amount
    })
    print("✅ Expense added successfully!\n")

def view_expense():
    if not expenses:
        print("❌ No expenses found\n")
        return
    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']}")
    print()

def total_expense():
    total=sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Eexpense: ₹{total}\n")

def highest_spending():
    if not expenses:
        print("❌ No expenses found\n")
        return
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"\n🔥 Highest Spending : {highest['date']} → ₹{highest['amount']}\n")

def monthly_expense(): 
    month = input("Enter month(MM):") 
    total=0
    for exp in expenses:
        if exp["date"].split("-")[1] == month: 
            total += exp["amount"]
    print(f"\n🗓️ Total expense for month {month}: ₹{total}\n") 

def menu():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Highest Spedning Day")
        print("5. Monthly Expense")
        print("6. Exit")

        choice= input("Choose (1-6):")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()  
        elif choice == "3":
            total_expense()  
        elif choice == "4":
            highest_spending()
        elif choice == "5":
            monthly_expense()  
        elif choice == "6":
            print("👋 Exiting..")
            break
        else:
            print("❌ Invalid Choice\n")

menu()     
