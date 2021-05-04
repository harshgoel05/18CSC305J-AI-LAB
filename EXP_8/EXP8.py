nouns={0:"cat",1:"dog",2:"human",3:"whale",4:"dolphin",5:"pigeon",6:"eagle",7:"mammal",8:"bird",9:"animal"}
adj=[[0 for i in range(10)] for j in range(10)]


adj[0][7]=1
adj[1][7]=1
adj[2][7]=1
adj[3][7]=1
adj[4][7]=1
adj[5][8]=1
adj[6][8]=1
adj[7][9]=1
adj[8][9]=1



def dfs(v):
    print(nouns[v])
    vis[v]=1
    for i in range(10):
        if adj[v][i] and not vis[i]:
            dfs(i)
print("Implementation of 'is a' relation\n")
for i in range(7):
    print(f"Relation {i+1}")
    vis=[0 for i in range(10)]
    if vis[i]==0:
        vis[i]=1
        dfs(i)