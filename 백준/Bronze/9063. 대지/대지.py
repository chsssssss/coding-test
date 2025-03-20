T = int(input())
dots = []
X = []
Y = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0
for t in range(T):
    x, y = map(int, input().split())
    dots.append((x,y))

for x, y in dots:
    X.append(x)
    Y.append(y)
print((max(X) - min(X)) * (max(Y) - min(Y)))