from core.view.base_view import BaseView

class BookView(BaseView):
    def display_book_added(self, title):
        print(f"Buku '{title}' berhasil ditambahkan, yeayy!")

    def display_book_updated(self, title):
        print(f"Buku '{title}' berhasil diubah!")
        # print("=======================")

    def display_book_borrowed(self, title):
        print(f"Buku '{title}' berhasil dipinjam!")
        # print("=======================")
    
    def display_book_returned(self, title):
        print(f"Buku '{title}' berhasil dikembalikan!")
        # print("=======================")
    
    def display_book_deleted(self, title):
        print(f"Buku '{title}' berhasil dihapus!")

    def display_book_details(self, book):
        print("\nDetail buku ini:")
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Status: {book[2]}")
    
    def display_books(self, books):
        index = 1
        if not books:
            print("Tidak ada buku ditemukan.")
        else:
            print("\n===================")
            print("Daftar Semua Buku:")
            for book in books:
                print(f"{index}. Judul: {book[0]}, Penulis: {book[1]}, Status: {book[2]}")
                index += 1
            print("===================\n")

    def display_available_books(self, books):
        index = 1
        if not books:
            print("Tidak ada buku ditemukan.")
        else:
            available_books = []
            print("\n===================")
            print("Daftar Buku yang Dapat Dipinjam (Tersedia):")
            for book in books:
                if book[2] == 'tersedia':
                    print(f"{index}. Judul: {book[0]}, Penulis: {book[1]}, Status: {book[2]}")
                    available_books.append(book)
                index += 1
            if len(available_books) < 1:
                print("Tidak ada buku yang tersedia")
                print("===================\n")
                return False
            print("===================\n")
        return True
    
    def display_borrowed_books(self, books):
        index = 1
        if not books:
            print("Tidak ada buku ditemukan.")
        else:
            borrowed_books = []
            print("\n===================")
            print("Daftar Buku yang telah dipinjam (Dipinjam):")
            for book in books:
                if book[2] == 'dipinjam':
                    print(f"{index}. Judul: {book[0]}, Penulis: {book[1]}, Status: {book[2]}")
                    borrowed_books.append(book)
                index += 1
            if len(borrowed_books) < 1:
                print("Tidak ada buku yang tersedia")
                print("===================\n")
                return False
            print("===================\n")
        return True