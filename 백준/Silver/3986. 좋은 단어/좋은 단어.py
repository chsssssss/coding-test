N = int(input())
count = 0
for _ in range(N):
    stack = []
    s = list(input())
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        count += 1
print(count)