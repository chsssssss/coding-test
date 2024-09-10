def solution(n):
    answer = 0
    i = 1
    while n >= factorial(i):
        answer = i
        i += 1
    return answer

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n - 1)