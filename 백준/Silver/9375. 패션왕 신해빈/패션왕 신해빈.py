test_case = int(input())

for _ in range(test_case):
    clothes = {}
    result = 1

    n = int(input())
    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    
    for count in clothes.values():
        result *= (count + 1)
    print(result - 1)