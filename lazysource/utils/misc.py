import re
from string import Formatter

from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError


class KeyStrFormatter(Formatter):
    
    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            try:
                return kwds[key]
            except KeyError:
                return key
        else:
            return Formatter.get_value(key, args, kwds)

  
class ExitExeption(Exception):
    pass


class EditScnMenuValidator(Validator):
    def __init__(self, menu_ops) -> None:
        self._menu_ops = menu_ops
        super().__init__()
    
    def validate(self, doc: Document):
        text = doc.text
        
        if text and text not in self._menu_ops:
            raise ValidationError(message="Input must be one of the available options",
                                  cursor_position=3)


class EditScnDateValidator(Validator):
    
    def validate(self, doc: Document):
        text = doc.text
        r = re.compile('\d{4}-\d{2}-\d{2}')
        if r.match(text) is None:
            raise ValidationError(message="Input must be in format YYYY-MM-DD",
                                cursor_position=3)