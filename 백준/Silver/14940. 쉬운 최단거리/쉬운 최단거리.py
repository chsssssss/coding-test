from collections import deque
N, M = map(int, input().split())
graph = []
dist = [[-1] * M for _ in range(N)]

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            start = (i, j)

queue = deque()
queue.append(start)
dist[start[0]][start[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()