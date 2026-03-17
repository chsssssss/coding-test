import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    parts = input().split()
    command = parts[0]
    num = parts [1] if len(parts) > 1 else None
    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        

