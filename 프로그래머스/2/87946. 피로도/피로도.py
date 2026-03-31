def solution(k, dungeons):
    max_dungeons = 0

    for i in range(len(dungeons)):
        visited = [False] * len(dungeons)
        if dungeons[i][0] <= k:
            max_dungeons = max(max_dungeons, dfs(visited, dungeons, k, i, 1))
    return max_dungeons

def dfs(visited, dungeons, k, node, cnt):
    visited[node] = True
    max_cnt = cnt
    k -= dungeons[node][1]
    
    for idx, (min_fatigue, use_fatigue) in enumerate(dungeons):
        if not visited[idx] and min_fatigue <= k:
            max_cnt = max(max_cnt, dfs(visited, dungeons, k, idx, cnt+1))
            visited[idx] = False
    return max_cnt