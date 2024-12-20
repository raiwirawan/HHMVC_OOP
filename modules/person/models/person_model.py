class PersonModel:
    def __init__(self):
        self.persons = []

    def add_person(self, name):
        """Menambahkan nama ke dalam daftar"""
        if name and name not in self.persons:
            self.persons.append(name)
            return True
        return False

    def get_persons(self):
        """Mendapatkan daftar semua nama"""
        return self.persons

    def remove_person(self, name):
        """Menghapus nama dari daftar"""
        if name in self.persons:
            self.persons.remove(name)
            return True
        return False