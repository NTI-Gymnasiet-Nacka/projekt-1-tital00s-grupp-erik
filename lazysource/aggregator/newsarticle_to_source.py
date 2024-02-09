import requests
from newspaper import Article
from newspaper.utils import BeautifulSoup

class Newsarticle():
    """
    params:
        title: the headline/title  str|Any
        authors: the author/authors seprated with ;  str
        d_o_p: date of publication YYYY-MM-DD  str|None
        publisher: new of newspaper/publisher  str|None
    """
    
    def __init__(self, base_url: str) -> None:
        
        self.base_url = base_url
        self._raw_html = requests.get(base_url)
        
        self.setup()
        
    def setup(self):
        
        soup = BeautifulSoup(self._raw_html.text, "html.parser")
        
        article = Article('')
        article.download(self._raw_html.content)
        article.parse()
        
        self.title = article.title
        
        if article.publish_date is not None:
            date_time = str(article.publish_date)
            self.d_o_p = date_time.split()[0]
        else:
            self.d_o_p = None
            
        self._raw_authors = article.meta_data.get("author")
        if self._raw_authors in (False, None):
            self._raw_authors = article.authors
        if isinstance(self._raw_authors, str):
            self._raw_authors = [self._raw_authors]
        self.authors = ''.join([f"{author};" for author in self._raw_authors])
        
        self.publisher = None
        try:
            self.publisher = article.meta_data.get("article").get("publication")
        except AttributeError:
            self.publisher = None
        if self.publisher is None:
            try:
                self.publisher = article.meta_data.get("og").get("site_name")
            except AttributeError:
                self.publisher = None
            if self.publisher is None:
                self.publisher = article.meta_data.get("application-name")
