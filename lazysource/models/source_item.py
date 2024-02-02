from datetime import date
from datetime import datetime

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
    
    id_: Mapped[str] = mapped_column(primary_key=True)
    catagory: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(9999))
    d_o_p: Mapped[date] = mapped_column(Date()) #date of pulication
    authors: Mapped[str] = mapped_column(String(9999)) 
    publisher: Mapped[str] = mapped_column(String(9999))
    page_nums: Mapped[str] = mapped_column(String(9999))
    edition: Mapped[str] = mapped_column(String(9999))
    url: Mapped[str] = mapped_column(String(9999))
    access_date: Mapped[date] = mapped_column(Date(),
                                              default=date.today())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )
    
    
    def from_dict(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise AttributeError(f"Unkown: {key: vaue}")
            setattr(self, key, value)

    def to_dict(self):
        source_data = { 
                       "catagory": self.catagory,
                       "title ":  self.title,
                       "d_o_p":  self.d_o_p,
                       "authors": self.authors,
                       "publisher":  self.publisher,
                       "page_nums":  self.page_nums,
                       "edition": self.edition,
                       "url": self.url,
                       "access_date": self.access_date
                       }
        return source_data
