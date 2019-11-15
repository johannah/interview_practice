graph = {'A':set(['B', 'C']), 
         'B':set(['D', 'E', 'F']), 
         'C':set(['G', 'H', 'I']), 
         'D':set(['J']), 
         'E':set([]), 
         'F':set([]), 
         'G':set([]), 
         'H':set(['K']), 
         'I':set(['L']), 
         'J':set([]),
         'K':set([]),
         'L':set([]),}

def bfs_reverse_level(graph, start):
    # visit every node in graph using bfs
    queue = [start]
    visited = [] 
    levels = {0:['A']}
    level = 0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex]-set(visited))
            if not vertex in levels[level]:
                print(levels[level][::-1])
                level += 1
            if level+1 not in levels.keys():
                levels[level+1] = []
            levels[level+1].extend(list(graph[vertex]))
    return visited


def bfs_reverse_nodes(graph, start):
    queue = [start]
    visited = []
    levels = {0:['A']}
    level = 0
    while queue: 
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex]-set(visited))
            print(list(graph[vertex])[::-1])



#bfs_reverse_level(graph, 'A')
bfs_reverse_nodes(graph, 'A')

