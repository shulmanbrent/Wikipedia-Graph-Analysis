
from Page_SNAP import Page_SNAP

def BFS(start_page_name, end_page_name):
    goal = Page_SNAP(end_page_name, None)
    q = list()
    start = Page_SNAP(start_page_name, None)
    q.append(start)
    total = 0
    visited = set()
    while(len(q) != 0):
        total += 1
        print total
        page = q.pop()
        visited.add(page)
        children = page.getChildren()
        for child in children:
            if child in visited:
                continue
            print child.title
            if child == goal:
                print("\nFound!\n\n")
                while (child.parent != None):
                    print(child.title + "<-")
                    child = child.parent
                print child.title
                return
            else:
                q.insert(0, child)
