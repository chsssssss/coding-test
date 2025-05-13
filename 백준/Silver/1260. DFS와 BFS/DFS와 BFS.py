from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_answer.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def dfs(graph, v, visited):
    visited[v] = True
    dfs_answer.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)
dfs_answer = []
bfs_answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for neighbors in graph:
    neighbors.sort()
dfs(graph, V, dfs_visited)
bfs(graph, V, bfs_visited)

print(' '.join(map(str, dfs_answer)))
print(' '.join(map(str, bfs_answer)))