# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# Use BFS/DFS starting from node until search stops(false) or we find destination(true)

def route_between_nodes(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    adj_list = {i:[] for i in range(n)}
    if source == destination: return True
    for x,y in edges:
        adj_list[x].append(y)
    stack = []
    visited = set()
    stack.append(source)
    while stack:
        node = stack.pop()
        for curr in adj_list[node]:
            if curr == destination:
                return True
            if  curr not in visited:
                stack.append(curr)
                visited.add(curr)
    return False



edges = [[0,1],[1,2],[2,0]]
edges1 = [[0,1],[0,2],[3,5],[5,4],[4,3]]


# print(route_between_nodes(3,edges,0,2))
print(route_between_nodes(6,edges1,0,5))