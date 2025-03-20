X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())
X4= 0
Y4 = 0

if X1 == X2:
    X4 = X3
elif X2 == X3:
    X4 = X1
else:
    X4 = X2

if Y1 == Y2:
    Y4 = Y3
elif Y2 == Y3:
    Y4 = Y1
else:
    Y4 = Y2
print(X4, Y4)