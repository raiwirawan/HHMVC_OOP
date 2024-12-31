class BaseView:
    def display(self, message):
        print(message)
    
    def display_error(self, error):
        print(f"Error: {error}")
    
    def display_list(self, items):
        if not items:
            print("Tidak ada hal yg ditemukan")
        else:
            for item in items:
                print(item)