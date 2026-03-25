N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append((x, y))
result.sort()

for x, y in result:
    print(x, y)