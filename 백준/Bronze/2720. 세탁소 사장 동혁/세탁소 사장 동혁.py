T = int(input())
for test_case in range(1, T + 1):
    C = int(input())
    quater = 0
    dime = 0
    nickel = 0
    penny = 0

    quater = C // 25
    C = C % 25
    dime = C // 10
    C = C % 10
    nickel = C // 5
    penny = C % 5
    print(f"{quater} {dime} {nickel} {penny}")