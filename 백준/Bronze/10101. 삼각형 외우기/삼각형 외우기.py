d1 = int(input())
d2 = int(input())
d3 = int(input())

if sum([d1, d2, d3]) != 180:
    print("Error")
elif d1 == 60 and d2 == 60 and d3 == 60:
    print("Equilateral")
elif d1 == d2 or d2 == d3 or d1 == d3:
    print("Isosceles")
else:
    print("Scalene")