from itertools import permutations
def solution(numbers):
    result = set()
    for i in range(1, len(numbers) + 1):
        for number in set(permutations(numbers, i)):
            num = int("".join(number))
            if num > 1 and is_prime(num) :
                result.add(num)

    return len(result)

def is_prime(number):
    i = 2
    if number < 2:
        return True
    else:
        while i < number:
            if number % i == 0:
                return False
            i += 1
    return True