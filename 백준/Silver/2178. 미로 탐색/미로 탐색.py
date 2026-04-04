from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
queue = deque([(0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]

while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
        nx, ny = dx + x, dy + y
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
print(graph[N-1][M-1])