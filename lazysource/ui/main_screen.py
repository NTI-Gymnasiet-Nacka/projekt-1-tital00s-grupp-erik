from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea, Button

class MainScreen:
    def __init__(self, app):
        self.app = app # the Application instance 
        self.setup_layout()

    def setup_layout(self):
        self.text_area = TextArea()
        self.exit_button = Button(text="Exit", handler=self.exit)
        self.layout = Layout(HSplit([self.text_area, self.exit_button]))

    def exit(self):
        self.app.exit()
