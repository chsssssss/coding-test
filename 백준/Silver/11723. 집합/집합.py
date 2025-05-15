import sys
input = sys.stdin.readline
M = int(input())
S = []
for _ in range(M):
    command = list(input().split())
    if command[0] == 'add':
        if int(command[1]) not in S:
            S.append(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in S:
            S.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.append(int(command[1]))
    elif command[0] == 'all':
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    else:
        S.clear()