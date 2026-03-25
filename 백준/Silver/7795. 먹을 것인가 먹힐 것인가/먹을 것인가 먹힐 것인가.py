import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    result = 0
    j = 0

    for i in range(a):
        while j < b and B[j] < A[i]:
            j += 1
        result += j

    print(result)