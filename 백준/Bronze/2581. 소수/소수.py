M = int(input())
N = int(input())
num = []
for i in range(M, N+1):
    if i < 2:  # 2 미만은 소수가 아님
        continue
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))