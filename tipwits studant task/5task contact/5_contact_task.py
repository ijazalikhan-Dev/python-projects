
import json
import os

filename = "contacts.json"

def load_contacts():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

def view_contacts(contacts):
    for c in contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

def search_contact(contacts):
    term = input("Enter name or phone: ")
    for c in contacts:
        if term in c["name"] or term in c["phone"]:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

def update_contact(contacts):
    name = input("Enter name to update: ")
    for c in contacts:
        if c["name"] == name:
            c["phone"] = input("New Phone: ")
            c["email"] = input("New Email: ")
            save_contacts(contacts)
            break

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    contacts[:] = [c for c in contacts if c["name"] != name]
    save_contacts(contacts)

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
