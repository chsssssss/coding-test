B, N = input().split()
B = B[::-1]
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for i in range(len(B)-1, -1, -1):
    result += num.index(B[i]) * int(N)**i
print(result)