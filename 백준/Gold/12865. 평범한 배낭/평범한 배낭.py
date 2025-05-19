N, K = map(int, input().split())
items = []
dp = [0] * (K+1)
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

for weight, value in items:
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)
print(dp[K])