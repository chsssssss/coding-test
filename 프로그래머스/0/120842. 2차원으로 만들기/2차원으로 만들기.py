def solution(num_list, n):
    answer = []
    cnt = 1
    temp = []
    for i in num_list:
        temp.append(i)
        cnt += 1
        if cnt == n + 1:
            answer.append(temp)
            temp = []
            cnt = 1
        
    return answer