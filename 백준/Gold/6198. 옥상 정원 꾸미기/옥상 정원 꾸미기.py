N = int(input())
buildings = [int(input()) for i in range(N)]
stack = []
result = 0

for i in range(N):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
        
    result += len(stack)
    stack.append(buildings[i])

print(result)
