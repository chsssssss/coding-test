def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i, j in wires:
        visited = [False] * (n + 1)
        graph[i].remove(j)
        graph[j].remove(i)
        
        count = dfs(i, graph, visited)
        
        answer = min(answer, abs((n - count) - count))
        
        graph[i].append(j)
        graph[j].append(i)
    
    return answer

def dfs(node, graph, visited):
    visited[node] = True
    cnt = 1
    
    for next in graph[node]:
        if not visited[next]:
            cnt += dfs(next, graph, visited)
    return cnt
        
        
    
    

    