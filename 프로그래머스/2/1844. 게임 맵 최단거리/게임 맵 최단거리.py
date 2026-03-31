from collections import deque
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[False] * m for _ in range(n)]
    
    queue = deque([(n-1, m-1)])
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0 and not visited[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    if maps[0][0] > 1:
        answer = maps[0][0]
    return answer
    
    
    