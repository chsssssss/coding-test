from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([])
visited = [[False] * M for _ in range(N)]
max_result = -float('inf')

def dfs(x, y, depth, sum):
    global max_result
    
    if depth == 4:
        max_result = max(max_result, sum)
        return 

    for dx, dy in directions:
        nx, ny = dx + x, dy + y
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, sum + matrix[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, sum + matrix[nx][ny])
            visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, matrix[i][j])
        visited[i][j] = False
print(max_result)