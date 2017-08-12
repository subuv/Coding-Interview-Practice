graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    explored = []
    queue = [start]
 
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
 
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

bfs(graph, 'A') # {'A', 'C', 'B', 'F', 'E', 'D'}
