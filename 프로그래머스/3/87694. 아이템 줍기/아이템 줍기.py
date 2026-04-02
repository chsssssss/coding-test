from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    queue = deque([(characterX * 2, characterY * 2, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * 102 for _ in range(102)]
    field = [[-1] * 102 for _ in range(102)]
    distance = 0
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    while queue:
        x, y, dis = queue.popleft()
        visited[x][y] = True
        print(x, y, dis)
        if x == itemX * 2 and y == itemY * 2:
            return dis // 2
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if not visited[nx][ny] and field[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny, dis + 1))
    
    return dis