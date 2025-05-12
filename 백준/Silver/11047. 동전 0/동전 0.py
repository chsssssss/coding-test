N, K = map(int, input().split())
coins = []
answer = 0
for _ in range(N):
    a = int(input())
    coins.append(a)

for i in coins[::-1]:
    if K >= i:
        answer += K // i
        K %= i

print(answer)
