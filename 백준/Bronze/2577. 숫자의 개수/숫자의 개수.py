A = int(input())
B = int(input())
C = int(input())
num = str(A*B*C)
result = [0] * 10

for i in num:
    result[int(i)] += 1

for j in result:
    print(j)