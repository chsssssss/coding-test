N, M = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0
S = [0] * N
C = [0] * M
S[0] = numbers[0]
for i in range(1, N):
	S[i] = S[i-1] + numbers[i]
	
for i in range(N):
	remainder = S[i] % M
	if remainder == 0:
		count += 1
	C[remainder] += 1

for i in range(M):
	if C[i] > 1:
		count += (C[i] * (C[i] - 1) // 2)
print(count)