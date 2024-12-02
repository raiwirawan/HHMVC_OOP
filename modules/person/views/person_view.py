class PersonView:
    def display_persons(self, persons):
        """Menampilkan daftar nama"""
        if not persons:
            print("Tidak ada nama dalam daftar.")
        else:
            print("\n--- Daftar Nama ---")
            for index, person in enumerate(persons, 1):
                print(f"{index}. {person}")
            print(f"Total nama: {len(persons)}")

    def show_add_success(self, name):
        """Menampilkan pesan berhasil menambahkan nama"""
        print(f"✅ Nama '{name}' berhasil ditambahkan.")

    def show_add_error(self, name):
        """Menampilkan pesan gagal menambahkan nama"""
        print(f"❌ Nama '{name}' sudah ada atau tidak valid.")

    def show_remove_success(self, name):
        """Menampilkan pesan berhasil menghapus nama"""
        print(f"✅ Nama '{name}' berhasil dihapus.")

    def show_remove_error(self, name):
        """Menampilkan pesan gagal menghapus nama"""
        print(f"❌ Nama '{name}' tidak ditemukan.")

    def show_menu(self):
        """Menampilkan menu pilihan"""
        print("\n=== Manajemen Nama ===")
        print("1. Tampilkan Daftar Nama")
        print("2. Tambah Nama")
        print("3. Hapus Nama")
        print("4. Keluar")