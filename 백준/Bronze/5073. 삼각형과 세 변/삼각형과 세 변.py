while True:
    length = list(map(int, input().split()))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    length.sort()
    if length[2] < length[0] + length[1]:
        if length[0] == length[1] and length[1] == length[2]:
            print("Equilateral")
        elif length[0] == length[1] or length[1] == length[2] or length[0] == length[2]:
            print("Isosceles")
        elif length[0] != length[1] and length[1] != length[2] and length[2] != length[0]:
            print("Scalene")
    else:
        print("Invalid")