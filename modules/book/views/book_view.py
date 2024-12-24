from core.view.base_view import BaseView

class BookView(BaseView):
    def display_book_added(self, title):
        print(f"Book '{title}' added successfully!")

    def display_book_updated(self, title):
        print(f"Book '{title}' updated successfully!")
        print("=======================")
    
    def display_book_deleted(self, title):
        print(f"Book '{title}' deleted successfully!")

    def display_book_details(self, book):
        print("\nCurrent book details:")
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
    
    def display_books(self, books):
        index = 1;
        if not books:
            print("No books found.")
        else:
            print("\n===================")
            print("Book List:")
            for book in books:
                print(f"{index}. Title: {book[0]}, Author: {book[1]}")
                index += 1
            print("===================\n")