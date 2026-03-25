import sys
input = sys.stdin.readline
N = int(input())
result = [0] * N
for i in range(N):
    num = int(input())
    result[i] = num
result.sort()
for i in range(N):
    print(result[i])