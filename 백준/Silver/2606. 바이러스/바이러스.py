def dfs(v):
    visited[v] = True
    count = 1
    for neighbor in graph[v]:
        if  not visited[neighbor]:
            count += dfs(neighbor)
    return count

N = int(input())
M = int(input())
visited = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(dfs(1) - 1)