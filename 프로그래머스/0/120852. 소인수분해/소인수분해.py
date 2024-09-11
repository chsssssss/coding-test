def solution(n):
    answer = []
    i = 2
    while(n != 1):
        if n % i == 0:
            n = n // i
            if i not in answer:
                answer.append(i)
            i = 2
        else:
            i += 1
    return answer