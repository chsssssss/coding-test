T = int(input())
P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 101):
    P.append(P[i - 3] + P[i - 2])
for _ in range(T):
    N = int(input())
    print(P[N-1])