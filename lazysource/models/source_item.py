from datetime import date
from datetime import datetime
from typing import List

from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass


class SourceItem(Base):
    __tablename__ = "source_items"
    
    id_: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(9999), nullable=True)
    # d_o_p: Mapped[str] = mapped_column(String(10)) #date of pulication
    d_o_p: Mapped[date] = mapped_column(Date(), nullable=True) #date of pulication
    authors: Mapped[str] = mapped_column(String(9999), nullable=True) 
    publisher: Mapped[str] = mapped_column(String(9999), nullable=True)
    page_nums: Mapped[str] = mapped_column(String(9999), nullable=True)
    edition: Mapped[str] = mapped_column(String(9999), nullable=True)
    url: Mapped[str] = mapped_column(String(9999), nullable=True)
    access_date: Mapped[date] = mapped_column(Date(),
                                              default=date.today())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    
    
    def from_dict(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise AttributeError(f"Unkown: {key}: {value}")
            else:
                setattr(self, key, value)

    def to_dict(self):
        source_data = { 
                       "id": self.id_,
                       "category": self.category,
                       "title":  self.title,
                       "d_o_p":  self.d_o_p,
                       "authors": self.authors,
                       "publisher":  self.publisher,
                       "page_nums":  self.page_nums,
                       "edition": self.edition,
                       "url": self.url,
                       "access_date": self.access_date
                       }
        return source_data

def authors_to_list(authors:str|None) -> List[str]:
    # ALL Authors shall be added with trailing semicolon
    return authors.split(sep=";") if authors is not None else []
    
    
class SourceData:
    def __init__(self, **kwargs) -> None:
        id = kwargs.get("id")
        if id is not None:
            self.id = id
        else:
            self.id = None
        self.category = kwargs.get("category")
        self.title = kwargs.get("title")
        self._d_o_p = kwargs.get("d_o_p")
        if self._d_o_p and isinstance(self._d_o_p, str):
            self.d_o_p = self._d_o_p

        self._authors: str | None = kwargs.get("authors")
        self.publisher: str | None = kwargs.get("publisher")
        self.page_nums = kwargs.get("page_nums")
        self.edition = kwargs.get("edition")
        self.url = kwargs.get("url")
        self._access_date = kwargs.get("access_date")

        if self._access_date and isinstance(self._access_date, str):
            self.access_date = self._access_date

    @property 
    def authors(self) -> List[str]:
        return authors_to_list(self._authors)

    @property
    def access_date(self):
        return self._access_date.strftime('%Y-%m-%d') if self._access_date else None

    @access_date.setter
    def access_date(self, value):
        if value is None:
            self._access_date = None
        else:
            try:
                self._access_date = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError(f"Access Date must be in 'YYYY-MM-DD' format or None, got '{value}'")
    @property
    def d_o_p(self):
        return self._d_o_p.strftime('%Y-%m-%d') if self._d_o_p else None

    @d_o_p.setter
    def d_o_p(self, value):
        if value is None:
            self._d_o_p = None
        else:
            try:
                self._d_o_p = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError(f"Date Of Publication must be in 'YYYY-MM-DD' format or None, got '{value}'")

    def to_dict(self):
        source_data = { 
                       "id_": self.id,
                       "category": self.category,
                       "title":  self.title,
                       "d_o_p":  self._d_o_p,
                       "authors": self._authors,
                       "publisher":  self.publisher,
                       "page_nums":  self.page_nums,
                       "edition": self.edition,
                       "url": self.url,
                       "access_date": self._access_date
                       }
        return source_data

    def export_dict(self):
        source_data = { 
                       "category": self.category,
                       "title":  self.title,
                       "d_o_p":  self.d_o_p,
                       "authors": self.authors,
                       "publisher":  self.publisher,
                       "page_nums":  self.page_nums,
                       "edition": self.edition,
                       "url": self.url,
                       "access_date": self.access_date
                       }
        return source_data
