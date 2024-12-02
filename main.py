from modules.book.controllers.book_controller import BookController

def main():
    book_controller = BookController()

    while True:
        print("\nBook Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Delete Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_controller.add_book(title, author)
        
        elif choice == '2':
            book_controller.list_books()
        
        elif choice == '3':
            title = input("Enter book title to delete: ")
            book_controller.remove_book(title)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()