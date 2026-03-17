T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    a = [[b for b in range(1, n+1)]]
    for i in range(k):
        x = []
        for j in range(n):
            x.append(sum(a[i][:j+1]))
        a.append(x)
    
    print(a[-1][-1])