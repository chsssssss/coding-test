N = int(input())
stairs = []
D = [0] * N
for _ in range(N):
    score = int(input())
    stairs.append(score)
if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    D[0] = stairs[0]
    D[1] = stairs[0] + stairs[1]
    D[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        D[i] = (max(D[i - 3] + stairs[i - 1] + stairs[i], D[i-2] + stairs[i]))
    print(D[N-1])