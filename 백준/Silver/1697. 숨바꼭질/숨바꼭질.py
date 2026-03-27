from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()

        if x == K:
            print(visited[x])
            break

        for next in [x - 1, x + 1, 2 * x]:
            if 0 <= next < MAX and visited[next] == 0:
                queue.append(next)
                visited[next] = visited[x] + 1

bfs(N)