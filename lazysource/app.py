from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.table import Table

from lazysource.database.db_manager import DatabaseManager
from lazysource.utils.copier import copy_to_clipboard
from lazysource.models.source_item import SourceData
from lazysource.utils.extract_as_harvard import build_export_string

class App:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.console = Console()
        
    def main_window(self):
        self.console.print("[cyan]Main window")
        options = ["View all sources", "Import source", "Export source"]
        completer = WordCompleter(options)
        formatted_options = '/'.join(f"[yellow]{option}[/yellow]" for option in options)
        self.console.print(f'Options: {formatted_options}')
        choice = prompt(">> ", completer=completer)
        
        try:
            if choice == options[0]:
                self.view_all_sources()
            elif choice == options[1]:
                self.export_source_screen()
            elif choice == options[2]:
                self.export_source_screen()
            else:
                raise ValueError("Invalid command")
            
        except ValueError as e:
            self.console.print(f'[red]{e}')
            self.run()
            
        
    def view_all_sources(self):
        pass
    
    def import_source_screen(self):
        pass

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
                # html_reference = "<p><i>Author Last Name, Author First Initial.</i> (Year Published). <i>Title of Document</i>. Retrieved from http://URL</p>"
                
                try: 
                    sources = self.db_manager.get_all_sources()
                    # run with source to html func here
                    

                    export_strings = [build_export_string(source.export_dict()) for source in sources] 
                    # self.console.print(export_strings) # Test

                    # test
                    # export_strings = [html_reference]*5

                    for string in export_strings:
                        # print_formatted_text(HTML(string))
                        print(string)

                    self.console.print("Looks good?") 
                    options = ["Yes", "No"]
                    completer = WordCompleter(options)
                    choice = prompt(">> ", completer=completer)

                    if choice == options[0]:
                        # sorts export strings by first char in A-Z 
                        # Concate that list of strings into singular string
                        # Copy to clipboard 

                        export_strings.sort() # By first char from A-Z
                        export_string = ''.join(export_strings) # Build a singular list
                        res = copy_to_clipboard(export_string)
                        #res = ""
                        self.console.print(f'[bold green]{res}[/bold green]')
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
            
            
    def run(self):
        self.main_window()


if __name__ == "__main__":
    app = App()
    source_data_examples = [
            {
                "category": "book",
                "title": "The Pragmatic Programmer: Your Journey To Mastery",
                "d_o_p": "1999-10-30",
                "authors": "Andrew Hunt;David Thomas;",
                "publisher": "Addison-Wesley Professional",
                "page_nums": "320",
                "edition": "1st",
                "url": "https://example.com/pragmaticprogrammer",
                "access_date": "2024-02-10",
                },
            {
                "category": "book",
                "title": "Deep Learning for Generic Object Detection: A Survey",
                "d_o_p": "2019-01-15",
                "authors": "Li Liu;Wanli Ouyang;Xiaogang Wang;Paul Fieguth;Jie Chen;Xinwang Liu;Matt Pietikäinen;",
                "publisher": "International Journal of Computer Vision",
                "page_nums": "45-67",
                "edition": "",
                "url": "https://example.com/deeplearningobjectsurvey",
                "access_date": "2024-02-12",
                },
            {
                "category": "article",
                "title": "Attention is All You Need",
                "d_o_p": "2017-06-12",
                "authors": "Ashish Vaswani;Noam Shazeer;Niki Parmar;Jakob Uszkoreit;Llion Jones;Aidan N. Gomez;Łukasz Kaiser;Illia Polosukhin;",
                "publisher": "NIPS",
                "page_nums": "5998-6008",
                "edition": "",
                "url": "https://example.com/attentionneedy",
                "access_date": "2024-02-11",
                }
            ]

    source_data_objects = [SourceData(**data) for data in source_data_examples]

    # app.db_manager.add_source(source_data_objects[-1].to_dict())
    for source in source_data_objects:
        # app.db_manager.add_source(source.to_dict())
        pass
    app.run()


