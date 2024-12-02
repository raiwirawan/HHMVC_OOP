from modules.person.models.person_model import PersonModel
from modules.person.views.person_view import PersonView

class PersonController:
    def __init__(self):
        self.model = PersonModel()
        self.view = PersonView()

    def run(self):
        """Menjalankan aplikasi"""
        while True:
            self.view.show_menu()
            
            try:
                choice = input("Pilih menu (1-4): ")

                if choice == '1':
                    # Tampilkan daftar nama
                    persons = self.model.get_persons()
                    self.view.display_persons(persons)

                elif choice == '2':
                    # Tambah nama
                    name = input("Masukkan nama: ").strip()
                    if self.model.add_person(name):
                        self.view.show_add_success(name)
                    else:
                        self.view.show_add_error(name)

                elif choice == '3':
                    # Hapus nama
                    name = input("Masukkan nama yang akan dihapus: ").strip()
                    if self.model.remove_person(name):
                        self.view.show_remove_success(name)
                    else:
                        self.view.show_remove_error(name)

                elif choice == '4':
                    # Keluar dari aplikasi
                    print("Terima kasih. Sampai jumpa!")
                    break

                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")