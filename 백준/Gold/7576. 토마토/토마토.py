from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque([])
    result = 0
    
    if all(all(cell != 0 for cell in row) for row in graph):
        return 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                graph[nx][ny] = 1
                queue.append((nx, ny))
                result = visited[nx][ny]
    
    for row in graph:
        if 0 in row:
            return -1
        
    return result

print(bfs())