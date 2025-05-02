import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] * (N+1)]
S = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    table.append(row)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + table[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 -1][y1 - 1])
