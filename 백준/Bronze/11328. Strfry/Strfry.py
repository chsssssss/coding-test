N = int(input())
for _ in range(N):
    a, b = map(str, input().split())
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    if a == b:
        print("Possible")
    else:
        print("Impossible")