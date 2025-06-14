
import json
import os

def load_data():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open("inventory.json", "w") as f:
        json.dump(data, f)

def add_product(data):
    name = input("Enter product name: ")
    pid = input("Enter product ID: ")
    qty = int(input("Enter quantity: "))
    data.append({"name": name, "id": pid, "qty": qty})
    save_data(data)
    print("Product added.\n")

def view_inventory(data):
    if not data:
        print("No products found.\n")
    else:
        for p in data:
            print(f"Name: {p['name']}, ID: {p['id']}, Quantity: {p['qty']}")
        print()

def update_quantity(data):
    pid = input("Enter product ID to update: ")
    for p in data:
        if p["id"] == pid:
            p["qty"] = int(input("Enter new quantity: "))
            save_data(data)
            print("Quantity updated.\n")
            return
    print("Product not found.\n")

def delete_product(data):
    pid = input("Enter product ID to delete: ")
    for p in data:
        if p["id"] == pid:
            data.remove(p)
            save_data(data)
            print("Product deleted.\n")
            return
    print("Product not found.\n")

def search_product(data):
    key = input("Enter product Name or ID to search: ").lower()
    found = False
    for p in data:
        if key == p["id"].lower() or key == p["name"].lower():
            print(f"Name: {p['name']}, ID: {p['id']}, Quantity: {p['qty']}")
            found = True
    if not found:
        print("Product not found.\n")
    else:
        print()

def main():
    data = load_data()
    while True:
        print("1. Add Product\n2. View Inventory\n3. Update Quantity\n4. Delete Product\n5. Search Product\n6. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_product(data)
        elif choice == "2":
            view_inventory(data)
        elif choice == "3":
            update_quantity(data)
        elif choice == "4":
            delete_product(data)
        elif choice == "5":
            search_product(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()

