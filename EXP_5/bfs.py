from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]


def addEdges():  #node, dest, cost
	addEdgetoGraph(0, 1, 3)
	addEdgetoGraph(0, 2, 6)
	addEdgetoGraph(0, 3, 5)
	addEdgetoGraph(1, 4, 9)
	addEdgetoGraph(1, 5, 8)
	addEdgetoGraph(2, 6, 12)
	addEdgetoGraph(2, 7, 14)
	addEdgetoGraph(3, 8, 7)
	addEdgetoGraph(8, 9, 5)
	addEdgetoGraph(8, 10, 6)
	addEdgetoGraph(9, 11, 1)
	addEdgetoGraph(9, 12, 10)
	addEdgetoGraph(9, 13, 2)


def addEdgetoGraph(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))

def best_first_search(source, target, n):
	visited = [0] * n
	visited[source] = True
	pq = PriorityQueue()
	pq.put((0, source))
	while pq.empty() == False:
		u = pq.get()[1]
		print(u, end=" ")
		if u == target:
			break

		for v, c in graph[u]:
			if (visited[v] == False ):
				visited[v] = True
				pq.put((c, v))
	print()



addEdges()
source = 3 
target = 12
best_first_search(source, target, v)
