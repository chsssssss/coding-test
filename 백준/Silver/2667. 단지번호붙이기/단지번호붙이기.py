from collections import deque
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * (N+1) for _ in range(N)]
result = []
count = 0

def bfs(x, y):
    global count
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    result.append(count)
    return x, y

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i, j)
result.sort()
print(len(result))
print('\n'.join(map(str, result)))