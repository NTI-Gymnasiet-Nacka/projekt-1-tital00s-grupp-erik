import requests
import re
from newspaper import Article
from newspaper.utils import BeautifulSoup

class Newsarticle():
    
    def __init__(self, base_url) -> None:
        
        self.base_url = base_url
        self.raw_html = requests.get(base_url)
        
        self.setup()
        
    def setup(self):
        
        soup = BeautifulSoup(self.raw_html.text, "html.parser")
        
        article = Article('')
        article.download(self.raw_html.content)
        article.parse()
        
        self.title = article.title
        if article.publish_date is not None:
            date_time = str(article.publish_date)
            self.d_o_p = date_time.split()[0]
        else:
            self.d_o_p = None
        self.authors = article.authors
        self.publisher = article.meta_data.get("og").get("site_name")
        

#testing stuff, more test need to be done
base_url = 'https://hard-drive.net/hd/ian-miles-cheong-first-recipient-of-neuralink-thanks-to-inherently-low-risk-of-damaging-intellect/'

new_article = Newsarticle(base_url=base_url)
print(new_article.authors)
print(new_article.publisher)
