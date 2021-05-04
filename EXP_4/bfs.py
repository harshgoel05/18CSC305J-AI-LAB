def inputGraph():
    n = int(input("No of Nodes: "))
    g = {}
    for i in range(n):
        node = input("Node " + str(i) + " -> ")
        l = list(input("Adjacent node for  " + node + "->").split(","))
        if l == ['']:
            l = []
        g[node] = l
    print("Entered Graph:-> " + str(g))
    return g

def BFSTraversal(visited, graph, node, l):
	visited.append(node)
	queue.append(node)
	while queue:
		s = queue.pop(0)
		l.append(s)
		for neighbour in graph[s]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
	return l

visited = []
queue  = []
graph = inputGraph()
start_node = list(graph.keys())[0]
l = BFSTraversal(visited, graph, start_node, l=[])
print("BFS traversal of the graph:", str(l))
ser = input("Enter Node to be searched -> ")
if ser in l:
    print("Node exists in the given graph.")
else:
    print("Node doesn't exist in the given graph.")