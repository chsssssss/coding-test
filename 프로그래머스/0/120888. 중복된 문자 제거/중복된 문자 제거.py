def solution(my_string):
    answer = ''
    strlist = []
    for i in my_string:
        if i not in strlist:
            answer += i
        strlist.append(i)
    return answer