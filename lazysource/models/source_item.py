from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass


class SourceItem(Base):
    __tablename__ = "source_items"
    
    id_: Mapped[str] = mapped_column(primary_key=True)
    catagory: Mapped[str] = mapped_column(String(30))
    title = Mapped[str] = mapped_column(String(9999))
    d_o_p = Mapped[str] = mapped_column[String(10)] #date of pulication
    authors: Mapped[str] = mapped_column(String(9999)) 
    publisher: Mapped[str] = mapped_column(String(9999))
    page_nums: Mapped[str] = mapped_column(String(9999))
    edition: Mapped[str] = mapped_column(String(9999))
    url: Mapped[str] = mapped_column(String(9999))
    access_date: Mapped[str] = mapped_column(String(10))
    #created at
    #updated at
    
    
    
    

