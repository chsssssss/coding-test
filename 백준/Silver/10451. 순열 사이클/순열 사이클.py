from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    count = 0

    for i in range(1, N+1):
        graph[numbers[i]].append(i)
        graph[i].append(numbers[i])

    def dfs(x):
        visited[x] = True
        next = numbers[x]

        if not visited[next]:
            dfs(next)
    

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)