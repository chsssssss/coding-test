from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
heights = {num for row in graph for num in row}
max_safe_zones = 1

def bfs(x, y, h):
    queue = deque([(x, y)])
    while queue:
        curr_x, curr_y = queue.popleft()
        visited[x][y] = True
        for dx, dy in directions:
            nx = dx + curr_x
            ny = dy + curr_y
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > h and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return count


for h in heights:
    visited = [[False] * (N) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
                if graph[i][j] > h and not visited[i][j]:
                    bfs(i, j, h)
                    count += 1
    if count > max_safe_zones:
        max_safe_zones = count
print(max_safe_zones)