T = int(input())

for _ in range(T):
    stack = []
    vps = list(input())
    for i in vps:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        print("YES")
    else:
        print("NO")