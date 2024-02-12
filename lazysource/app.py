from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from rich.console import Console

from lazysource.database.db_manager import DatabaseManager
from lazysource.utils.copier import copy_to_clipboard

class App:
    def __init__(self):
        self.db_manager = DatabaseManager()

        self.console = Console()

    def export_source_screen(self):
        # Ask which sources to export?
        self.console.print("[cyan]Export Source Screeen") 
        options = ["All", "Go to home"]
        completer = WordCompleter(options)
        formatted_options = '/'.join(f"[yellow]{option}[/yellow]" for option in options)
        self.console.print(f'Options: {formatted_options}')
        choice = prompt(">> ", completer=completer)
        
        try:
            if choice == options[0]:
                # Get all sources from db and run each through
                # export source utility func

                # Test reference
                html_reference = "<p><i>Author Last Name, Author First Initial.</i> (Year Published). <i>Title of Document</i>. Retrieved from http://URL</p>"
                try: 
                    sources = self.db_manager.get_all_sources()
                    # run with to html source  func here
                    export_strings = [source for source in sources] 
                    # test
                    export_strings = [html_reference]*5 

                    for string in export_strings:
                        print_formatted_text(HTML(string))

                    self.console.print("Looks good?") 
                    options = ["Yes", "No"]
                    completer = WordCompleter(options)
                    choice = prompt(">> ", completer=completer)

                    if choice == options[0]:
                        # TODO: sort export strings by first char in A-Z 
                        # Concate that list of strings into singular string
                        # Copy to clipboard 

                        export_string = ''.join(export_strings)
                        res = copy_to_clipboard(export_string)
                        self.console.print(f'[green]{res}')
                        # self.main_screen() # Switch to main screen

                    elif choice == options[1]:
                        # switch to edit screen
                        # self.edit_source_screen()
                        pass
                    else:
                        raise ValueError("Invalid command")
                    
                except Exception as e:
                    self.console.print(f"[red]Error: {e}")
                    self.export_source_screen()

            elif choice == options[-1]:
                # self.main_screen()
                pass

            else:
                raise ValueError('Invalid command')

        except ValueError as e:
            self.console.print(f'[red]{e}')
            self.export_source_screen()


if __name__ == "__main__":
    app = App()
    app.export_source_screen()


