import sys

from lazysource.app import App


def main():
    path = sys.argv[0] # always exists, this the path from which script was called
    url = None
    if len(sys.argv) > 1:
        url = sys.argv[1]


    if url is not None:
        print("Tryies to add given url as source and start doing the scraping and all")
        print(f"Doing scraping... in path: {path}")
        print(f"of URL: {url}")
        # pass in the url to the app
    app = App()
    app.run()

if __name__ == "__main__":
     main()
