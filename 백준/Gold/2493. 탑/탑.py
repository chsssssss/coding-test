N = int(input())
tops = list(map(int, input().split()))
stack = []
result = []

for i in range(N):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)
    stack.append((i, tops[i]))
    
print(' '.join(map(str, result)))