T = int(input())
D=[1, 2, 4]
for i in range(3, 12):
    D.append(D[i-3] + D[i-2] + D[i-1])
for _ in range(T):
    N = int(input())
    print(D[N-1])