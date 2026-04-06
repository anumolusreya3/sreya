library = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    library.append({"name": name, "author": author})
    print("Book added successfully")

def view_books():
    if not library:
        print("No books available")
    else:
        for b in library:
            print(f"Book: {b['name']}, Author: {b['author']}")

def issue_book():
    name = input("Enter book name to issue: ")
    for b in library:
        if b["name"] == name:
            library.remove(b)
            print("Book issued")
            return
    print("Book not found")

def return_book():
    name = input("Enter book name to return: ")
    author = input("Enter author name: ")
    library.append({"name": name, "author": author})
    print("Book returned")

while True:
    print("\n1. Add Book\n2. View Books\n3. Issue Book\n4. Return Book\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
