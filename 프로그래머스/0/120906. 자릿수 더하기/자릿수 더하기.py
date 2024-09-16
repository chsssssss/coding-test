def solution(n):
    answer = 0
    for i in range(0, len(str(n))):
        answer += int(str(n)[i])
    return answer