from copy import deepcopy
from textwrap import dedent

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from rich.console import Console

from lazysource.database.db_manager import DatabaseManager
from lazysource.models.source_item import SourceData
from lazysource.utils.misc import KeyStrFormatter, ExitExeption, EditScnMenuValidator, EditScnDateValidator
        

class App:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.console = Console()
        self._ksf = KeyStrFormatter()
        
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