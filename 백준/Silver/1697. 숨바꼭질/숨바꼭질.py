from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX

def bfs(start):
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        if pos == K:
            return visited[pos]
        for next_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)
print(bfs(N))