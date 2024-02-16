from typing import Dict, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from lazysource.models.source_item import Base, SourceData, SourceItem

class ItemNotFoundError(Exception):
    pass

class DatabaseManager:
    def __init__(self, db_url="sqlite:///test.db") -> None:
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()

    def get_source(self, source_item_id:int):
        with self.get_session() as session:
            item = session.query(SourceItem).filter(SourceItem.id_ == source_item_id).one_or_none()
            if item is None:
                raise ItemNotFoundError(f"Item_source with id: {source_item_id} not found")
            return item

    def add_source(self, source_data:SourceData):
        with self.get_session() as session:
            try:

                item = SourceItem()
                item.from_dict(**source_data.to_dict())
                session.add(item)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def update_source(self, source_data: SourceData):
        with self.get_session() as session:
            try:
                item = self.get_source(source_data.id)
                if item:
                    item.from_dict(**source_data.to_dict())
                    session.merge(item)
                    session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def delete_source(self, source_item_id: int):
        with self.get_session() as session:
            try:
                item = self.get_source(source_item_id)
                if item:
                    session.delete(item)
                    session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def get_all_sources(self) -> List[SourceData]:
        with self.get_session() as session:
            sources = session.query(SourceItem).all()
            return [SourceData(**source.to_dict()) for source in sources]

if __name__ == "__main__":
    db = DatabaseManager()
    source = SourceData()
    source.category = "Idk"
    source.title = "yoo"
    db.add_source(source)

    sources = db.get_all_sources()
    print(sources)
    # db.get_source(sources[0].id)
    source = sources[1]
    source.title = "New title"
    db.update_source(source)

    sources = db.get_all_sources()
    for source in sources:
        print(source.id, source.title)

