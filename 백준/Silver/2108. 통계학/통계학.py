import sys
input = sys.stdin.readline
N = int(input())
num = [int(input()) for _ in range(N)]
dic = {}
m = 0
M = []
num.sort()
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    if m < dic[i]:
        m = dic[i]
for key, val in dic.items():
    if val == m:
        M.append(key)
M.sort()
if len(M) > 1:
    m = M[1]
else:
    m = M[0]

print(round(sum(num) / N))
print(num[(N//2)])
print(m)
print(max(num) - min(num))
