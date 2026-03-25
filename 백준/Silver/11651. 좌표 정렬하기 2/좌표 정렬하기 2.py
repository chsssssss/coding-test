N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append((x, y))
result.sort(key= lambda x: (x[1], x[0]))

for x, y in result:
    print(x, y)