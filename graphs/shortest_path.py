graph =  {'A':set(['B', 'C']), 
          'B':set(['D']), 
          'C':set(['D']), 
          'D':set([]),
          }

def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

def bfs_paths(graph, start, end):
    """
     return shortest path from start to end in graph
    """
    # queue is list of tuples containing (vertex, path)
    assert start in graph.keys()
    assert end in graph.keys()
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for nx in graph[vertex]-set(path):
            if nx == end:
                yield path+[nx]
            else:
                queue.append((nx,path+[nx]))

def bfs_shortest_path(graph, start, end):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for nx in graph[vertex]-set(path):
            if nx == end:
                return path+[nx]
            else:
                queue.append((nx,path+[nx]))
print(bfs(graph, 'A'))
print([p for p in bfs_paths(graph, 'A', 'D')])
print([p for p in bfs_shortest_path(graph, 'A', 'D')])

