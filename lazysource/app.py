from copy import deepcopy
from textwrap import dedent

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.table import Table

from lazysource.utils.misc import KeyStrFormatter, ExitExeption, EditScnMenuValidator, EditScnDateValidator
from lazysource.database.db_manager import DatabaseManager
from lazysource.utils.copier import copy_to_clipboard
from lazysource.models.source_item import SourceData
from lazysource.utils.extract_as_harvard import build_export_string
from lazysource.utils.utils import escape_html

"""
TODO: 
1) Empty strings after actions
2) Import screen
3) Let user pick source to export
4) Edit sources
"""

class App:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.console = Console()
        self._ksf = KeyStrFormatter()
    
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
        
    def edit_source_scn(self, source: SourceData):
        _source = deepcopy(source)

        _menu_ops = (
            "Title",
            "DOP",
            "Authors",
            "Publisher",
            "Page Numbers",
            "Edition",
            "Save",
            "Exit"
        )
        _main_menu_completer = WordCompleter(_menu_ops)
        
        _menu_str = dedent("""\
                           Title: {title}
                           DOP: {d_o_p}
                           Authors: {authors}
                           Publisher: {publisher}
                           Page Numbers: {page_nums}
                           Edition: {edition}

                           Save     Exit"""
        )
        
        while True:
            self.console.print("[yellow]Edit Source Screen")
            self.console.print(self._ksf.format(_menu_str, **vars(_source)))
        
            try:
                _choice = prompt(">> ", completer=_main_menu_completer, validator=EditScnMenuValidator(_menu_ops))
            
                if _choice == "Title":
                    _entry = prompt("Enter new title\n>> ")
                    _source.title = _entry
                elif _choice == "DOP":
                    _entry = prompt(">> ", validator=EditScnDateValidator())
                    _source.d_o_p = _entry
                elif _choice == "Authors":
                    edit_authors = _source.authors
                    _aut_menu_ops = (
                        "Add",
                        "Remove",
                        "Back"
                        )    
                    self.console.print(''.join([f"{op}\n" for op in _aut_menu_ops]))    
                    aut_choice = prompt(">> ", completer=WordCompleter(_aut_menu_ops),
                                        validator=EditScnMenuValidator(_aut_menu_ops))
                    if aut_choice == "Add":
                        _entry == prompt(">> ")
                        edit_authors.append(_entry)
                    elif aut_choice == "Remove":
                        _entry == prompt(">> ", completer=WordCompleter(_source.authors),
                                        validator=EditScnMenuValidator(_source.authors))
                        edit_authors.remove(_entry)
                    elif aut_choice == "Back":
                        pass
                    authors_str = ''.join([f"{author};" for author in edit_authors])
                    _source._authors = authors_str[:-1]
                elif _choice == "Publisher":
                    _entry = prompt("Enter new publisher\n>> ")
                    _source.publisher = _entry
                elif _choice == "Page Numbers":
                    _entry = prompt("Enter new page numbers\n>> ")
                    _source.page_nums = _entry
                elif _choice == "Edition":
                    _entry = prompt("Enter new edition\n>> ")
                    _source.edition = _entry
                elif _choice == "Save":
                    self.db_manager.update_source(_source)
                    raise ExitExeption
                elif _choice == "Exit":
                    raise ExitExeption  
                
            except ExitExeption:
                break
            
        self.main_window()        
        
    def view_all_sources(self):
        sources = self.db_manager.get_all_sources() # List[SourceData]
        table = Table()
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Authors")
        for source in sources:
            table.add_row(str(source.id), source.title, source._authors)
        # fetch all sources
        # loopa source for sources
        # row add source.id source.authors, source.title
        self.console.print(table)
        self.main_window()
    
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
                        print_formatted_text(HTML(escape_html(string)))

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
                        self.main_window() # Switch to main screen

                    elif choice == options[1]:
                        # switch to edit screen
                        # self.edit_source_screen()
                        raise NotImplementedError("Not implemented")
                        pass
                    else:
                        raise ValueError("Invalid command")
                    
                except Exception as e:
                    self.console.print(f"[red]Error: {e}")
                    self.export_source_screen()

            elif choice == options[-1]:
                self.main_window()
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
                "title":  "500 skämt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Aörk;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                },
            {
                "category": "article",
                "title":  "500 skämt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Börk;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                },
            {
                "category": "article",
                "title":  "500 skämt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Cörk;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                }
            ]

    source_data_objects = [SourceData(**data) for data in source_data_examples]

    # app.db_manager.add_source(source_data_objects[-1].to_dict())
    for source in source_data_objects:
        #app.db_manager.add_source(source)
        pass
    app.run()
