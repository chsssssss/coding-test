def solution(n):
    answer = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j == n:
                answer.append(i)
    return answer