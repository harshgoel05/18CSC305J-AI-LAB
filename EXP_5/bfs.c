#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
vector<vector<pi> > graph;

void addedge(int x, int y, int cost)
{
	graph[x].push_back(make_pair(cost, y));
	graph[y].push_back(make_pair(cost, x));
}

void best_first_search(int source, int target, int n)
{
	vector<bool> visited(n, false);
	priority_queue<pi, vector<pi>, greater<pi> > pq;
	pq.push(make_pair(0, source));
    visited[0]=true;
	while (!pq.empty()) {
		int x = pq.top().second;
	
		cout << x << " ";
		pq.pop();
		if (x == target)
			break;

		for (int i = 0; i < graph[x].size(); i++) {
			if (!visited[graph[x][i].second]) {
				visited[graph[x][i].second] = true;
				pq.push(graph[x][i]);
			}
		}
	}
}

int main()
{
	int v = 4;
	graph.resize(v);
	
	addedge(0,1,3);
	addedge(0,2,6);
	addedge(1,3,5);
	addedge(2,3,6);

	int source = 0;
	int target = 3;

	best_first_search(source, target, v);

	return 0;
}
