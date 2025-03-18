N = int(input())
num = list(map(int, input().split()))
result = 0
for i in num:
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt < 3 and i != 1:
        result += 1
print(result)