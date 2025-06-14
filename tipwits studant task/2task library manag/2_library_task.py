import os, json

BOOK_FILE = "books.json"

def load_books():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(BOOK_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    books = load_books()
    books.append({"title": title, "author": author, "isbn": isbn, "issued": False})
    save_books(books)
    print("Book added.")

def display_books():
    books = load_books()
    if not books:
        print("No books.")
        return
    for i, book in enumerate(books, 1):
        status = "Issued" if book["issued"] else "Available"
        print(f"{i}. {book['title']} - {book['author']} - {book['isbn']} - {status}")

def issue_book():
    isbn = input("Enter ISBN to issue: ")
    books = load_books()
    for book in books:
        if book["isbn"] == isbn:
            if book["issued"]:
                print("Already issued.")
            else:
                book["issued"] = True
                save_books(books)
                print("Issued.")
            return
    print("Not found.")

def return_book():
    isbn = input("Enter ISBN to return: ")
    books = load_books()
    for book in books:
        if book["isbn"] == isbn:
            if not book["issued"]:
                print("Not issued.")
            else:
                book["issued"] = False
                save_books(books)
                print("Returned.")
            return
    print("Not found.")

def search_book():
    q = input("Enter Title or ISBN: ").lower()
    books = load_books()
    for book in books:
        if q in book["title"].lower() or q == book["isbn"]:
            status = "Issued" if book["issued"] else "Available"
            print(f"{book['title']} - {book['author']} - {book['isbn']} - {status}")
            return
    print("Not found.")

def menu():
    while True:
        print("\n1. Add Book\n2. Display Books\n3. Issue Book\n4. Return Book\n5. Search Book\n6. Exit")
        choice = input("Choose: ")
        if choice == '1': add_book()
        elif choice == '2': display_books()
        elif choice == '3': issue_book()
        elif choice == '4': return_book()
        elif choice == '5': search_book()
        elif choice == '6': break
        else: print("Invalid.")

menu()


