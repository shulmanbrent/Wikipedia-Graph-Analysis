''' Final Project
- This file will before BFS on links to find path from one topic to another
'''

#import requests
#from bs4 import BeautifulSoup
from Page import Page


def BFS(wiki_page_url):
    goal = Page("http://en.wikipedia.org/wiki/Academic_discipline", None)
    q = list()
    goal = Page(wiki_page_url, None)
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

#def getNextLevel(wiki_page):
#    print wiki_page
#    r = requests.get(wiki_page)
#    soup = BeautifulSoup(r.text)
#    body = soup.find(id = "content")
#    links = list()
#    for l in body.findAll(href = True):
#        links.append(l['href'])
#    links = filter(lambda l: "/wiki/" in l[0:7], links)
#    links = map(lambda l: "http://en.wikipedia.org" + l, links)
#    return links
