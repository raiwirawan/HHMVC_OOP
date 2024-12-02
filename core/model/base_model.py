import os

class BaseModel:
    def __init__(self, database_file):
        self.database_file = database_file
        self.ensure_database_exists()
    
    def ensure_database_exists(self):
        if not os.path.exists(self.database_file):
            with open(self.database_file, 'w') as f:
                pass