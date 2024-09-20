def solution(sides):
    answer = 0
    for i in range(0, sides[0] + sides[1] + 1):
        if max(sides) > i:
            if i + min(sides) > max(sides):   
                answer += 1
        else:
            if min(sides) + max(sides) > i:
                print(i)
                answer += 1
    return answer