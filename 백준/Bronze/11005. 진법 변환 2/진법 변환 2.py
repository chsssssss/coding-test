N, B = input().split()
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
N = int(N)
B = int(B)
while N != 0:
    result.append(num[N % B])
    N = N // B

print(''.join(result[::-1]))