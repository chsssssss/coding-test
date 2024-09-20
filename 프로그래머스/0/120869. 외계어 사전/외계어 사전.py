def solution(spell, dic):
    answer = 2
    for i in dic:
        if sorted(i) == sorted(spell):
            answer = 1

            
    return answer