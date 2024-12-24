from core.model.base_model import BaseModel
from config.config import Config
from modules.book.views.book_view import BookView

class BookModel(BaseModel):
    def __init__(self):
        super().__init__(Config.DATABASE['books_file'])
        self.view = BookView()
    
    def add_book(self, title, author, status):
        try:
            with open(self.database_file, 'a') as f:
                f.write(f"{title},{author},{status}\n")
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
    
    def update_book(self, book_index):
        try:
            with open(self.database_file, 'r') as file:
                books = file.readlines()
            
            if book_index < 0 or book_index >= len(books):
                print("Invalid book number!")
                return
            
            current_book = books[book_index].strip().split(',')
            
            self.view.display_book_details(current_book)
            
            new_title = input("Enter new title (press Enter to keep current): ").strip()
            new_author = input("Enter new author (press Enter to keep current): ").strip()
            new_status = input("Enter new status (press Enter to keep current): ").strip()

            new_title = new_title if new_title else current_book[0]
            new_author = new_author if new_author else current_book[1]
            new_status = new_status if new_status else current_book[2]

            updated_book = f"{new_title},{new_author},{new_status}\n"
            
            books[book_index] = updated_book
            
            with open(self.database_file, 'w') as file:
                file.writelines(books)

            print("\n=======================")
            print(f"{current_book[0]} -> {new_title}")
            print(f"{current_book[1]} -> {new_author}")
            print(f"{current_book[2]} -> {new_status}")
            
            return True
        except Exception as e:
            return False
    
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