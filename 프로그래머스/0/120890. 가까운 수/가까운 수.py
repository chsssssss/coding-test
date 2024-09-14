def solution(array, n):
    answer = 0
    array.sort()
    gap = 0
    previous = 100
    for i in array:
        gap = abs(i - n)
        if gap < previous:
            previous = gap
            answer = i
    return answer