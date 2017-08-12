graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, vertex):
    stack = [vertex]
    visited = [vertex]
    while stack:
        try:
            vertex = min(list(set(graph[vertex]) - set(visited)))
            stack.append(vertex)
            visited.append(vertex)
        except:
            stack.pop()
            if (len(stack) > 0):
                vertex = stack[-1]
    print(visited)

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
