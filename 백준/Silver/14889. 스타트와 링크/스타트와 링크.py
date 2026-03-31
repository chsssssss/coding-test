N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')

def get_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                score += S[team[i]][team[j]]
    return score

def dfs(start, team):
    global min_diff

    if len(team) == N // 2:
        team_b = [i for i in range(N) if i not in team]
        min_diff = min(min_diff, abs(get_score(team) - get_score(team_b)))
        return
    
    for i in range(start, N):
        dfs(i+1, team + [i])

dfs(0, [])
print(min_diff)