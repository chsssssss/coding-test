N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
t_c = 0

for i in shirts:
    if i % T == 0:
        t_c += i // T
    else:
        t_c += ((i // T) + 1)
print(t_c)
print(sum(shirts) // P, sum(shirts) % P)