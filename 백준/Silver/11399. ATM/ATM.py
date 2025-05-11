N = int(input())
P = list(map(int, input().split()))
temp = 0
S = []
P.sort()
for i in P:
    temp += i
    S.append(temp)
print(sum(S))