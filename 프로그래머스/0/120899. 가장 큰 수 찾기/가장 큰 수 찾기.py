def solution(array):
    for i in range(0, len(array)):
        if array[i] == max(array):
            answer = [max(array), i]
    return answer