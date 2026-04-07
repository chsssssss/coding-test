import sys
imput = sys.stdin.readline
N = int(input())

length = 1
start = 1
result = 0

while start <= N:
    end = start * 10 -1
    if end > N:
        end = N

    result += (end - start + 1) * length

    start *= 10
    length += 1
print(result)