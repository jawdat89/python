# Given a directed acyclical graph, return a valid
# topological ordering of the graph. 
def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    visit = set()
    visiting = set()
    for i in range(1, n + 1):
        if not dfs(i, adj, visit, visiting, topSort):
            return []
        dfs(i, adj, visit, visiting, topSort)
    topSort.reverse()
    return topSort

def dfs(src, adj, visit, visiting, topSort):
    if src in visit:
        return True
    if src in visiting:
        return False# cycle
    visit.add(src)
    
    for neighbor in adj[src]:
        if not dfs(neighbor, adj, visit, visiting, topSort):
            return False
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)


# using defaultdict
from collections import defaultdict
def topologicalSort(edges, n):
    adj = defaultdict(list)
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    
    visited = set()
    visiting = set()

    def dfs(src: int) -> bool:
        if src in visited:
            return True
        if src in visiting:
            return False # cycle
        visiting.add(src)
        for neighbor in adj[src]:
            if not dfs(neighbor):
                return False # cycle
        visiting.remove(src)
        visited.add(src)
        topSort.append(src)
        return True
    
    for i in range(1, n + 1):
        if not dfs(i):
            return [] # cycle
    
    topSort.reverse()
    return topSort