# def solution(my_string):
#     answer = ''
#     for i in range(len(my_string), 0, -1):
#         answer += my_string[i - 1]
#     return answer
def solution(my_string):
    answer = ''
    for c in my_string:
        answer= c+answer
    return answer