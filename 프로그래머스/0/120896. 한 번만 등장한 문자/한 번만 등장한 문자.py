def solution(s):
    answer = ''
    str_list = {}
    for i in s:
        if i in str_list:
            str_list[i] += 1
        else:
            str_list[i] = 1
    
    for j in str_list:
        if str_list[j] == 1:
            answer += j

    return ''.join(sorted(answer))