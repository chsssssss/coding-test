N, M = map(int, input().split())

passwords = {}
result = []
for _ in range(N):
    address, pwd = input().split()
    passwords[address] = pwd

for _ in range(M):
    address = input()
    result.append(passwords[address])

for i in result:
    print(i)