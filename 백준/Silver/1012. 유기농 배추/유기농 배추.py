import sys
sys.setrecursionlimit(10000)

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                count += 1
    print(count)

