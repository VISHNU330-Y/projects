import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

DATA_FILE = "data.csv"

# Initialize CSV file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

def add_record(record_type, category, amount, description):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), record_type, category, amount, description])
    print(f"✅ {record_type} record added successfully!")

def show_summary():
    income_total = 0
    expense_total = 0
    category_expense = {}

    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row["Amount"])
            if row["Type"].lower() == "income":
                income_total += amt
            else:
                expense_total += amt
                cat = row["Category"]
                category_expense[cat] = category_expense.get(cat, 0) + amt

    balance = income_total - expense_total
    print("\n📊 Budget Summary:")
    print(f"Total Income: ${income_total:.2f}")
    print(f"Total Expenses: ${expense_total:.2f}")
    print(f"Balance: ${balance:.2f}")
    print("\nExpenses by Category:")
    for cat, amt in category_expense.items():
        print(f"  {cat}: ${amt:.2f}")

    # Visualize expenses with a pie chart
    if category_expense:
        plt.figure(figsize=(6,6))
        plt.pie(category_expense.values(), labels=category_expense.keys(), autopct="%1.1f%%", startangle=140)
        plt.title("Expenses by Category")
        plt.show()

def main():
    while True:
        print("\n=== Personal Budget Manager ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary & Chart")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Income Category (e.g., Salary, Gift): ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            add_record("Income", category, amount, description)

        elif choice == "2":
            category = input("Expense Category (e.g., Food, Rent, Travel): ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            add_record("Expense", category, amount, description)

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
