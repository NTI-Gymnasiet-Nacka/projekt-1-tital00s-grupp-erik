from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.panel import Panel

from lazysource.database.db_manager import DatabaseManager
from lazysource.models.source_item import SourceData


class App:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.console = Console()
        self.edit_screen_contents = "Source here"
        
    def edit_source_screen(self, source):
        self.console.print(Panel(str(self.edit_screen_contents), title="Edit Source"))
