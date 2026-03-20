N, K = map(int, input().split())
stu = {}
result = 0
for _ in range(N):
    S, Y = map(int, input().split())
    if (S, Y) in stu:
        stu[(S, Y)] += 1
    else:
        stu[(S, Y)] = 1

for key, val in stu.items():
    if val > K:
        result += (val + 1) // K
    else:
        result += 1

print(result)