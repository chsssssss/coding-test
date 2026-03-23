S = list(input())
stack = []
result = 0

temp = 1

for i in range(len(S)):
    if S[i] == '(':
        temp *= 2
        stack.append('(')

    elif S[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if S[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2

    elif S[i] == '[':
        temp *= 3
        stack.append('[')

    elif S[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if S[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0
print(result)