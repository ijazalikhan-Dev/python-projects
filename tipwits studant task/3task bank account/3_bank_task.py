

import json

import os

filename = "accounts.json"

def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f)

def create_account(data):
    acc = input("Account Number: ")
    if acc in data:
        print("Account already exists.")
    else:
        name = input("Name: ")
        data[acc] = {"name": name, "balance": 0, "history": []}
        print("Account created.")

def deposit(data):
    acc = input("Account Number: ")
    if acc in data:
        amount = float(input("Deposit Amount: "))
        data[acc]["balance"] += amount
        data[acc]["history"].append(f"Deposited {amount}")
        print("Amount deposited.")
    else:
        print("Account not found.")

def withdraw(data):
    acc = input("Account Number: ")
    if acc in data:
        amount = float(input("Withdraw Amount: "))
        if amount <= data[acc]["balance"]:
            data[acc]["balance"] -= amount
            data[acc]["history"].append(f"Withdrew {amount}")
            print("Amount withdrawn.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def check_balance(data):
    acc = input("Account Number: ")
    if acc in data:
        print("Balance:", data[acc]["balance"])
    else:
        print("Account not found.")

def show_history(data):
    acc = input("Account Number: ")
    if acc in data:
        print("History:", data[acc]["history"])
    else:
        print("Account not found.")

def main():
    data = load_data()
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History\n6. Exit (Goodbye)")
        choice = input("Choose: ")
        if choice == "1":
            create_account(data)
        elif choice == "2":
            deposit(data)
        elif choice == "3":
            withdraw(data)
        elif choice == "4":
            check_balance(data)
        elif choice == "5":
            show_history(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        save_data(data)

if __name__ == "__main__":
    main()
