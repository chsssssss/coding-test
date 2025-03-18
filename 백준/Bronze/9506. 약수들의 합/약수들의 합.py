N = []

while True:
    n = int(input())
    if n == -1:
        break
    N.append(n)

for i in N:
    result = []
    for j in range(1, i):
        if i % j == 0:
            result.append(j)
    if sum(result) == i:
        print(f"{i} = {' + '.join(map(str, result))}")
    else:
        print(f"{i} is NOT perfect.")