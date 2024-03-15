from lazysource.app import App
from lazysource.models.source_item import SourceData

if __name__ == "__main__":
    app = App()
    source_data_examples = [
            {
                "category": "book",
                "title":  "500 skamt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Aork;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                },
            {
                "category": "article",
                "title":  "500 skamt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Bork;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                },
            {
                "category": "article",
                "title":  "500 skamt om papperssortering",
                "d_o_p":  "2012-11-15",
                "authors": "Vidar Silas Cork;Eddie Ekbacke;William Carl Svensson",
                "publisher":  "Bonnier",
                "page_nums":  "21-22",
                "edition": "5",
                "url": "www.youtube.com/video",
                "access_date": "2012-11-21"
                }
            ]

    source_data_objects = [SourceData(**data) for data in source_data_examples]
    
    for source in source_data_objects:
        app.db_manager.add_source(source)
        
    app.run()
