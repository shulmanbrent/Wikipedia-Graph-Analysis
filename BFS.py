''' Final Project
- This file will before BFS on links to find path from one topic to another
'''

#import requests
#from bs4 import BeautifulSoup
from Page import Page

# Assumes it is given properly formatted Wikipedia page URL's
def BFS(start_page_url, end_page_url):
    goal = Page(end_page_url, None)
    q = list()
    goal = Page(start_page_url, None)
    q.append(goal)
    total = 0
    visited = set()
    while(len(q) != 0):
        total += 1
        page = q.pop()
        if page in visited:
            continue
        visited.add(page)
        children = page.getChildren()
        for child in children:
            if child == goal:
                print("\nFound!\n\n")
                while (page.parent != None):
                    print(page.title + "<-")
                return
            else:
                q.append(child)
