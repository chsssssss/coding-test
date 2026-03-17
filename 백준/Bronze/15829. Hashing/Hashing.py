L = int(input())
a = input()
M = 1234567891
r = 31
result = 0

for i in range(L):
    value = ord(a[i]) - ord('a') + 1
    result += (value * r**i) % M

print(result % M)