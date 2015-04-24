import requests
from bs4 import BeautifulSoup

class Page_Web(object):

    # Constructor
    def __init__(self, url, parent):
        self.url = url
        self.parent = parent


    def getChildren(self):
        print(self.url)

        # Get the html text of the page and parses with BeautifulSoup
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        body = soup.find(id = "content")

        # Gets link strings from html of the page
        children = set()
        for l in body.findAll(href = True):
            # Get link for "href" value and removes in-page location indicator
            l = l['href'].rsplit("#")[0]

            # Gets other wikipedia links
            if "/wiki/" in l[0:7]:
                # Formats the wikipedia links correctly
                l = "http://en.wikipedia.org" + l
                # Create new child page object with parent pointer set
                page = Page_Web(l, self)
                # Add child page to set of children
                children.add(page)

        return children

    def __eq__(self, page):
        # TODO: ADD ERROR TO THROW IF TYPES ARE NOT THE SAME

        return (page.url == self.url)

    def __hash__(self):
        return hash(self.url)
