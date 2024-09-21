def solution(lines):
    answer = 0
    test = [0] * 200
    for i in lines:
        for j in range(i[0], i[1]):
            test[j + 100] += 1
            
    for count in test:
        if count > 1:
            answer += 1
    return answer