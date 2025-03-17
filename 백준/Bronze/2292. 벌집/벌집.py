N = int(input())
room = 1
result = 1
while room < N:
    room += result * 6
    result += 1
print(result)
