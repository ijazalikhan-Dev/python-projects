import json
import os

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added.")

def view_expenses(expenses):
    for e in expenses:
        print(f"Date: {e['date']}, Category: {e['category']}, Amount: {e['amount']}")

def total_expenses(expenses):
    total = sum(e['amount'] for e in expenses)
    print(f"Total expenses: {total}")

def search_by_date(expenses):
    date = input("Enter date (YYYY-MM-DD) to search: ")
    for e in expenses:
        if e['date'] == date:
            print(f"Category: {e['category']}, Amount: {e['amount']}")

def category_summary(expenses):
    summary = {}
    for e in expenses:
        cat = e['category']
        summary[cat] = summary.get(cat, 0) + e['amount']
    for cat, amt in summary.items():
        print(f"Category: {cat}, Total: {amt}")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search by Date")
        print("5. Category Summary")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            search_by_date(expenses)
        elif choice == "5":
            category_summary(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()

