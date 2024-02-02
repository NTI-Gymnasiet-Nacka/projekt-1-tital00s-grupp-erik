from prompt_toolkit.key_binding import KeyBindings

from lazysource.types import Screen

"""
Define all global keybinings heeere and other goodies smoothies
Then keybindings can be defined within another config file, for the user,
like toml or yaml :)
"""
def setup_keybindings(callbacks):
    key_bindings = KeyBindings()

    @key_bindings.add('c-q')
    def exit_(event):
        event.app.exit()

    @key_bindings.add('c-s')
    def _(event):
        callbacks.get(Screen.EXPORT, lambda: None)()

    @key_bindings.add('c-h')
    def _(event):
        callbacks.get(Screen.MAIN, lambda: None)()

    return key_bindings
