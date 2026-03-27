V = int(input())
E = int(input())
graph = [[] * (V + 1) for _ in range(V + 1)]
edges = [map(int, input().split()) for _ in range(E)]
visited = [False] * (V + 1)
for x, y in edges:
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

dfs(1)
print(visited.count(True)-1)