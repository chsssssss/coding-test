T = int(input())
fac = []
num = 1
for i in range(1, 31):
    num *= i
    fac.append(num)
for _ in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else:
        print(fac[M-1] // (fac[N-1] * fac[M-N-1]))