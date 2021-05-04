def inputGraph():
    n = int(input("No of Nodes: "))
    g = {}
    for i in range(n):
        node = input("Node " + str(i) + " -> ")
        l = list(input("Adjacency Node for " + node + "->").split(","))
        if l == ['']:
            l = []
        g[node] = l
    print("Entered Graph:-> " + str(g))
    return g

def DFSTraversal(visited, graph, node, l):
    if node not in visited:
        l.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFSTraversal(visited, graph, neighbour, l)
    if len(visited) == len(graph.keys()):
        return l


graph = inputGraph()
visited = set()
start_node = list(graph.keys())[0]
l = DFSTraversal(visited, graph, start_node, l=[])
print("DFS Traversal:", str(l))
ser = input("Enter Node to be searched -> ")
if ser in l:
    print("Node exists in the given graph.")
else:
    print("Node doesn't exist in the given graph.")