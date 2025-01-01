from core.model.base_model import BaseModel
from config.config import Config
from modules.book.views.book_view import BookView

class BookModel(BaseModel):
    def __init__(self):
        super().__init__(Config.DATABASE['books_file'])
        self.view = BookView()
        self.statuses = {"dipinjam", "tersedia"}
    
    def add_book(self, title, author, status):
        try:
            if(title == "" or author == "" or status == ""):
                print("Judul, Penulis, dan Status buku tidak valid")
                return

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
            
            # validasi sudah ada di book_controller
            # if book_index < 0 or book_index >= len(books):
            #     print("Nomor buku tidak valid!")
            #     return
            
            current_book = books[book_index].strip().split(',')
            
            self.view.display_book_details(current_book)
            
            new_title = input("Masukkan judul baru (tekan Enter tidak mau ubah): ").strip()
            new_author = input("Masukkan penulis baru (tekan Enter tidak mau ubah): ").strip()
            new_status = input("Masukkan status baru (tekan Enter tidak mau ubah): ").strip()

            if new_status == "":
                new_status = current_book[2]

            if not self.validate_status(new_status):
                print("Status hanya boleh 'dipinjam' dan 'tersedia'")
                return False

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
    
    def borrow_book(self, book_index):
        try:
            with open(self.database_file, 'r') as file:
                books = file.readlines()
            
            current_book = books[book_index].strip().split(',')

            self.view.display_book_details(current_book)

            current_book[2] = "dipinjam"

            updated_book = f"{current_book[0]},{current_book[1]},{current_book[2]}\n"

            books[book_index] = updated_book

            with open(self.database_file, 'w') as file:
                file.writelines(books)

            print("\n=======================")
            print(f"{current_book[0]}")
            print(f"{current_book[1]}")
            print(f"{current_book[2]}")

            return True
        except Exception as e:
            return False
    
    def return_book(self, book_index):
        try:
            with open(self.database_file, 'r') as file:
                books = file.readlines()
            
            current_book = books[book_index].strip().split(',')

            self.view.display_book_details(current_book)

            current_book[2] = "tersedia"

            updated_book = f"{current_book[0]},{current_book[1]},{current_book[2]}\n"

            books[book_index] = updated_book

            with open(self.database_file, 'w') as file:
                file.writelines(books)

            print("\n=======================")
            print(f"{current_book[0]}")
            print(f"{current_book[1]}")
            print(f"{current_book[2]}")

            return True
        except Exception as e:
            return False
    
    def delete_book(self, book_index):
        try:
            with open(self.database_file, "r") as f:
                books = f.readlines()

            # validasi sudah ada di book_controller
            # if book_index < 0 or book_index >= len(books):
            #     print("Nomor buku tidak valid!")
            #     return
            
            books.pop(book_index)

            with open(self.database_file, "w") as f:
                f.writelines(books)
    
            return True
        except Exception as e:
            return False

    def validate_status(self, status):
        return status in self.statuses