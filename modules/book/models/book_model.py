from core.model.base_model import BaseModel
from config.config import Config

class BookModel(BaseModel):
    def __init__(self):
        super().__init__(Config.DATABASE['books_file'])
    
    def add_book(self, title, author):
        try:
            with open(self.database_file, 'a') as f:
                f.write(f"{title},{author}\n")
            return True
        except Exception as e:
            return False
    
    def get_books(self):
        try:
            with open(self.database_file, 'r') as f:
                books = [line.strip().split(',') for line in f.readlines()]
            return books
        except Exception as e:
            return []
    
    def delete_book(self, title):
        try:
            books = self.get_books()
            updated_books = [book for book in books if book[0] != title]
            
            with open(self.database_file, 'w') as f:
                for book in updated_books:
                    f.write(f"{book[0]},{book[1]}\n")
            return True
        except Exception as e:
            return False