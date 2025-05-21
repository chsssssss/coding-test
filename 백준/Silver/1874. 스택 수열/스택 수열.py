N = int(input())
stack = [i for i in range(1, N+1)]
num = [int(input()) for _ in range(N)]
S = []
n = 0
answer = []
i = 1
while i < N + 1:
    if S and S[-1] == num[n]:
        S.pop()
        n += 1
        answer.append('-')
    else:
        S.append(i)
        answer.append('+')
        i += 1

for _ in range(len(S)):
    if S and S[-1] == num[n]:
        S.pop()
        answer.append('-')
        n += 1

if S:
    print('NO')
else:
    print('\n'.join(answer))