def solution(babbling):
    can_babble = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        for babble in can_babble:
            word = word.replace(babble, " ")
        
        if word.strip() == "":
            count += 1

    return count