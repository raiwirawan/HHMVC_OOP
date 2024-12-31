from modules.book.models.book_model import BookModel
from modules.book.views.book_view import BookView

class BookController:
    def __init__(self):
        self.model = BookModel()
        self.view = BookView()
    
    def add_book(self, title, author, status):
        result = self.model.add_book(title, author, status)
        if result:
            self.view.display_book_added(title)
        else:
            self.view.display_error("Gagal untuk nambah buku")
    
    def list_books(self):
        books = self.model.get_books()
        self.view.display_books(books)

    def list_available_books(self):
        books = self.model.get_books()
        self.view.display_available_books(books)
 
    def update_book(self, book_index):
        with open(self.model.database_file, 'r') as file:
            books = file.readlines()

        if book_index < 0 or book_index >= len(books):
            print("Nomor buku tidak valid!")
            return
        
        book_title = books[book_index].strip().split(",")[0]
        
        result = self.model.update_book(book_index)

        if result:
            self.view.display_book_updated(book_title)
        else:
            self.view.display_error("Gagal ubah buku")

    def borrow_book(self, book_index):
        with open(self.model.database_file, 'r') as file:
            books = file.readlines()

        if book_index < 0 or book_index >= len(books):
            print("Nomor buku tidak valid!")
            return
        
        book_title = books[book_index].strip().split(",")[0]
        
        result = self.model.update_book(book_index)

        if result:
            self.view.display_book_updated(book_title)
        else:
            self.view.display_error("Gagal pinjam buku")
    
    def remove_book(self, book_index):
        with open(self.model.database_file, 'r') as file:
            books = file.readlines()

        if book_index < 0 or book_index >= len(books):
            print("Nomor buku tidak valid!")
            return
        
        book_title = books[book_index].strip().split(",")[0]

        result = self.model.delete_book(book_index)
        
        if result:
            self.view.display_book_deleted(book_title)
        else:
            self.view.display_error("Gagal hapus buku")

    def verify_books_empty(self):
        books = self.model.get_books()

        if not books:
            return True
        
    def validate_status(self, status):
        return self.model.validate_status(status)