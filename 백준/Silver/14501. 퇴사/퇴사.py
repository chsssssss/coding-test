N = int(input())
t = []
p = []
for _ in range(N):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    finish_day = i + t[i]
    
    if finish_day <= N:
        dp[i] = max(p[i] + dp[finish_day], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
    
print(dp[0])