def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    return answer

def dfs(computers, visited, node):
    visited[node] = True
    for next in range(len(computers)):
        if not visited[next] and computers[node][next] == 1:
            dfs(computers, visited, next)