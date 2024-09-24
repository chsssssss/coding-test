def solution(before, after):
    for i in before:
        if i in after:
            before = before.replace(i, "", 1)
            after = after.replace(i, "", 1) 
    if after == "":
        answer = 1
    else:
        answer = 0

    return answer