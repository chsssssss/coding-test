N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')
visited = [False] * (N + 1)
 
def dfs(start, curr, count, cost):
    global min_cost

    if cost >= min_cost:
        return
    
    if count == N:
        if graph[curr][start] != 0:
            min_cost = min(min_cost, cost + graph[curr][start])
        return
        
    for next in range(N):
        if not visited[next] and graph[curr][next] != 0:
            visited[next] = True
            dfs(start, next, count + 1, cost + graph[curr][next])
            visited[next] = False

visited[0] = True
dfs(0, 0, 1, 0)
print(min_cost)