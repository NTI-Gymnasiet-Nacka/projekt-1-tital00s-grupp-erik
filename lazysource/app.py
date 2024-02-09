from prompt_toolkit import prompt

from lazysource.database.db_manager import DatabaseManager

class App:
    def __init__(self):
        self.db_manager = DatabaseManager()


    def export_source(self):
        options = ["All good"]


