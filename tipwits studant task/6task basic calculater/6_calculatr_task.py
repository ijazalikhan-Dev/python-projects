
import json
import os

filename = "calc_history.json"

def load_history():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_history(history):
    with open(filename, "w") as file:
        json.dump(history, file)

def calculate(history):
    expr = input("Enter expression (e.g. 2 + 3): ")
    try:
        result = eval(expr)
        print("Result:", result)
        history.append({"expression": expr, "result": result})
        save_history(history)
    except:
        print("Invalid expression.")

def show_history(history):
    for h in history:
        print(f"{h['expression']} = {h['result']}")

def main():
    history = load_history()
    while True:
        print("\n1. New Calculation")
        print("2. View History")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            calculate(history)
        elif choice == "2":
            show_history(history)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
