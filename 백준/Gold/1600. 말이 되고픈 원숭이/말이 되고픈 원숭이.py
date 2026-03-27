import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
horses = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2)]

visited = [[[ -1 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 0

    while queue:
        row, column, k = queue.popleft()

        if row == H-1 and column == W - 1:
            return visited[row][column][k]

        for dx, dy in directions:
            nx, ny = dx + row, dy + column
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == 0:
                if visited[nx][ny][k] == -1:
                    visited[nx][ny][k] = visited[row][column][k] + 1
                    queue.append((nx, ny, k))

        if k < K:
            for dx, dy in horses:
                nx, ny = dx + row, dy + column
                if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == 0:
                    if visited[nx][ny][k + 1] == -1:
                        visited[nx][ny][k + 1] = visited[row][column][k] + 1
                        queue.append((nx, ny, k + 1))
    return -1
print(bfs())