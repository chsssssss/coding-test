from itertools import product

N, K_cnt = map(int, input().split())
K = set(map(str, input().split()))

length = len(str(N))
candidates = []

for l in range(length, 0, -1):
    for p in product(K, repeat=l):
        num = int("".join(p))
        if num <= N:
            candidates.append(num)
    if candidates:
        print(max(candidates))
        break