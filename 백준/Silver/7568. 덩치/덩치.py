N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
answer = []
for i in range(N):
    k = 1
    for j in range(N):
        if i == j:
            continue
        if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
            k += 1
    answer.append(k)
print(' '.join(map(str, answer)))