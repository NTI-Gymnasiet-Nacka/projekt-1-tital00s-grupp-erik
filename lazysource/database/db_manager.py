from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from lazysource.models.source_item import Base, SourceItem


class DatabaseManager:
    def __init__(self, db_url="sqlite:///test.db") -> None:
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()

    def get_source(self, source_item_id):
        with self.get_session() as session:
            return session.query(SourceItem).filter(SourceItem.id_ == source_item_id).one_or_none()

    def add_source(self, item:SourceItem):
        with self.get_session() as session:
            try:
                session.add(item)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def update_source(self, item_id:SourceItem.id_):
        with self.get_session() as session:
            try:
                item = self.get_source(item_id)
                if item:
                    session.merge(item)
                    session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def delete_source(self, item_id:SourceItem.id_):
        with self.get_session() as session:
            try:
                item = self.get_source(item_id)
                if item:
                    session.delete(item)
                    session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def get_all_sources(self):
        with self.get_session() as session:
            sources = session.query(SourceItem).all()
            return sources

if __name__ == "__main__":
    print("Do your testing here?")
