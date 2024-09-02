def solution(array):
    cnt = [0] * 1000

    for i in array:
        cnt[i] += 1

    max_count = max(cnt) 
    max_count_values = [i for i, x in enumerate(cnt) if x == max_count]

    if len(max_count_values) > 1:
        return -1
    else:
        return max_count_values[0]
