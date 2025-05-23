N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

def dfs(start, v):
    for neighbor in range(N):
        if not visited[neighbor] and G[v][neighbor] == 1:
            visited[neighbor] = True
            G[start][neighbor] = 1
            dfs(start, neighbor)

for i in range(N):
    visited = [False] * N
    dfs(i, i)

for i in range(N):
    print(" ".join(map(str, G[i])))