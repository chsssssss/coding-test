import sys
input = sys.stdin.readline
N = int(input())
result = []

for _ in range(N):
    num = int(input())
    result.append(num)
result.sort(reverse= True)
for i in range(N):
    print(result[i])