import os
from bs4 import BeautifulSoup

class Page_SNAP(object):

    # Constructor
    def __init__(self, title, parent):
        #f = open(os.getcwd() + title, 'r')
        self.title = title
        self.parent = parent
        #f.close()

    def getChildren(self):
        cwd = os.getcwd()
        try:
            f = open(os.path.join(cwd + self.title), 'r')
        except Exception:
            return set()
        soup = BeautifulSoup(f.read())
        body = soup.find(id = "content")
        if body == None:
            body = soup
        f.close()
        # Gets link strings from html of the page
        children = set()
        for l in body.findAll(href = True):

            s = l['href'].split('..')
            s = s[len(s) - 1]
            if "/wp/" not in s:
                continue
            s = '\\wpcd' + s.replace("/", "\\")
            print s
            page = Page_SNAP(s, self)
            # Add child page to set of children
            children.add(page)

        return children

    def __eq__(self, page):
        # TODO: ADD ERROR TO THROW IF TYPES ARE NOT THE SAME

        return (page.title == self.title)

    def __hash__(self):
        return hash(self.title)
