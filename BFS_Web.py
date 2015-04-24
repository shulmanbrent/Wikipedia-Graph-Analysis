''' Final Project
- This file will before BFS on links to find path from one topic to another
'''

from Page_Web import Page_Web

# Assumes it is given properly formatted Wikipedia page URL's
def BFS(start_page_url, end_page_url):
    goal = Page_Web(end_page_url, None)
    q = list()
    start = Page_Web(start_page_url, None)
    q.append(start)
    total = 0
    visited = set()
    while(len(q) != 0):
        total += 1
        page = q.pop()
        visited.add(page)
        children = page.getChildren()
        for child in children:
            if child in visited:
                continue
            if child == goal:
                print("\nFound!\n")
                while (child.parent != None):
                    print(child.url + "<-")
                    child = child.parent
                print child.url
                return
            else:
                q.insert(0, child)
