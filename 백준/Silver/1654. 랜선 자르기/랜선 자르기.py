import sys
input = sys.stdin.readline
K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
result = 0
start = 1
end = max(L)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in L:
        count += i // mid
    if count >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)