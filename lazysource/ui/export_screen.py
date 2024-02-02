from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea, Button

class ExportScreen:
    def __init__(self, app):
        self.app = app # the Application instance 
        self.setup_layout()

    def setup_layout(self):
        # Example
        self.text_area = TextArea()
        self.exit_button = Button(text="Export", handler=self.exit)
        self.layout = Layout(HSplit([self.text_area, self.exit_button]))

    def exit(self):
        self.app.exit()
