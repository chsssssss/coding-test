def solution(board):
    n = len(board)
    answer = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    danger_zone = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger_zone[i][j] = 1

                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        danger_zone[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if danger_zone[i][j] == 0:
                answer += 1

    return answer
