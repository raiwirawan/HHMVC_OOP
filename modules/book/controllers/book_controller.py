from modules.book.models.book_model import BookModel
from modules.book.views.book_view import BookView

class BookController:
    def __init__(self):
        self.model = BookModel()
        self.view = BookView()
    
    def add_book(self, title, author):
        result = self.model.add_book(title, author)
        if result:
            self.view.display_book_added(title)
        else:
            self.view.display_error("Failed to add book")
    
    def list_books(self):
        books = self.model.get_books()
        self.view.display_books(books)
    
    def remove_book(self, title):
        result = self.model.delete_book(title)
        if result:
            self.view.display_book_deleted(title)
        else:
            self.view.display_error("Failed to delete book")