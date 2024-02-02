from prompt_toolkit.application import Application

from lazysource.config import setup_keybindings
from lazysource.types import Screen
from lazysource.ui.main_screen import MainScreen
from lazysource.ui.export_screen import ExportScreen

class App:
    """
    No Layouts are built here, only used!
    Here is place only for the buisness logic, switching screens etc!
    but not the UI itself
    """
    def __init__(self):
        self.app = None
        self.setup()

    def setup(self):
        # Screen inits
        self.main_screen = MainScreen(self)
        self.export_screen = ExportScreen(self)

    def show_export_screen(self):
        if self.app is None:
            raise ValueError("No app started")

        self.app.layout = self.export_screen.layout
        self.app.invalidate()

    def show_main_screen(self):
        if self.app is None:
            raise ValueError("No app started")

        self.app.layout = self.main_screen.layout
        self.app.invalidate()

    def run(self):
        key_mappings = {
            Screen.MAIN: self.show_main_screen,
            Screen.EXPORT: self.show_export_screen,
        }
        self.app = Application(layout=self.main_screen.layout,
                                       key_bindings=setup_keybindings(key_mappings),
                                       full_screen=True)
        self.app.run()

if __name__ == "__main__":
    app = App()
    app.run()
