A, P = map(int, input().split())
D = []

i = 0
while True:
    next_val = 0
    if A in D:
        print(D.index(A))
        break
    else:
        D.append(A)
    
    for j in str(A):
        next_val += int(j) ** P
    A = next_val
    i += 1

