N, M = map(int, input().split())
a = set(input() for _ in range(N))
result = []

for _ in range(M):
    n = input()
    if n in a:
        result.append(n)

print(len(result))
for i in sorted(result):
    print(i)