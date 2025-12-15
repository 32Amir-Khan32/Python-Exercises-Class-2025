def add_book(library, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }
    library.append(book)
    print(f"Added '{title}' to the library")

def borrow_book(library, title):
    for book in library:
        if book["title"] == title:
            if book["available"]:
                book["available"] = False
                print(f"You have borrowed '{title}'")
                return True
            else:
                print(f"'{title}' is already borrowed")
                return False
    print(f"'{title}' not found in library")
    return False

def return_book(library, title):
    for book in library:
        if book["title"] == title:
            if not book["available"]:
                book["available"] = True
                print(f"Thank you for returning '{title}'")
                return True
            else:
                print(f"'{title}' was not borrowed")
                return False
    print(f"'{title}' not found in library")
    return False

def display_books(library):
    print("\nLibrary Catalog:")
    print("-" * 50)
    if not library:
        print("No books in library")
        return
    
    for i, book in enumerate(library, 1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {status}")

def library_system():
    library = []
    
    # Add some initial books
    add_book(library, "Python Programming", "John Smith", 2020)
    add_book(library, "Data Science", "Amir Khan", 2021)
    add_book(library, "Algorithms", "Sara Johnson", 2019)
    
    while True:
        print("\nLibrary Management System")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_books(library)
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            add_book(library, title, author, year)
        elif choice == '3':
            display_books(library)
            if library:
                title = input("Enter title to borrow: ")
                borrow_book(library, title)
        elif choice == '4':
            title = input("Enter title to return: ")
            return_book(library, title)
        elif choice == '5':
            print("Thank you for using the Library Management System")
            break
        else:
            print("Invalid choice. Please try again.")

# Uncomment to test interactively
# library_system()