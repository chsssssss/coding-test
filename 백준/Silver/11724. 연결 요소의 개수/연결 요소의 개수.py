
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)