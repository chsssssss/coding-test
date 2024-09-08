def solution(emergency):
    answer = []
    test = emergency.copy()
    test.sort()
    test.reverse()
    for i in emergency:
        answer.append(test.index(i) + 1)     
    return answer