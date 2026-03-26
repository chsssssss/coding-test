A, P = map(int, input().split())
visited = [0] * 250000

def get_next(n, p):
    return sum(int(digit) ** p for digit in str(n))

def dfs(n, count):
    if visited[n] != 0:
        return visited[n] - 1
    
    visited[n] = count

    next = get_next(n, P)
    return dfs(next, count + 1)

print(dfs(A, 1))