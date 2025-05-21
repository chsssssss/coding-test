import sys
def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
input = sys.stdin.readline
N = int(input())
solved = [int(input()) for _ in range(N)]
k = 0
answer = 0
solved.sort()
if N > 0:
    k = custom_round(N * 0.15)
    answer = custom_round(sum(solved[k:N-k]) / (N - 2*k))
print(answer)