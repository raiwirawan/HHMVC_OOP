from modules.book.controllers.book_controller import BookController

def main():
    book_controller = BookController()

    while True:
        print("\nSistem Kelola Buku")
        print("1. Tambah Buku")
        print("2. List Buku")
        print("3. Ubah Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Hapus Buku")
        print("7. Keluar")
        
        choice = input("Masukkan pilihanmu (1-7): ")

        if choice == '1':
            book_controller.list_books()
            title = input("Masukkan judul buku: ").strip()
            author = input("Masukkan penulis buku: ").strip()
            status = input("Masukkan status buku: ").strip()
            if not book_controller.validate_status(status):
                print("Gagal menambah buku")
                print("Status hanya bisa 'dipinjam' dan 'tersedia'")
                continue
            book_controller.add_book(title, author, status)
        
        elif choice == '2':
            book_controller.list_books()

        elif choice == '3':
            book_controller.list_books()
            if book_controller.verify_books_empty():
                continue
            book_index = int(input("Masukkan nomor buku yang ingin kamu ubah: ")) - 1
            book_controller.update_book(book_index)

        elif choice == '4':
            if not book_controller.list_available_books():
                continue
            if book_controller.verify_books_empty():
                continue
            book_index = int(input("Masukkan nomor buku yang ingin kamu pinjam: ")) - 1
            book_controller.borrow_book(book_index)
        
        elif choice == '5':
            if not book_controller.list_borrowed_books():
                continue
            if book_controller.verify_books_empty():
                continue
            book_index = int(input("Masukkan nomor buku yang ingin kamu kembalikan: ")) - 1
            book_controller.return_book(book_index)
        
        elif choice == '6':
            book_controller.list_books()
            if book_controller.verify_books_empty():
                continue
            book_index = int(input("Masukkan nomor buku yang ingin kamu hapus: ")) - 1
            book_controller.remove_book(book_index)
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi")

if __name__ == "__main__":
    main()