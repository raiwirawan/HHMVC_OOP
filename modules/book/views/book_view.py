from core.model.base_view import BaseView

class BookView(BaseView):
    def display_book_added(self, title):
        print(f"Book '{title}' added successfully!")
    
    def display_book_deleted(self, title):
        print(f"Book '{title}' deleted successfully!")
    
    def display_books(self, books):
        if not books:
            print("No books found.")
        else:
            print("Book List:")
            for book in books:
                print(f"Title: {book[0]}, Author: {book[1]}")