# def solution(numbers):
#     answer = 0
#     for i in range(0, len(numbers) - 1):
#         for j in range(i+1, len(numbers)):
#             if answer < numbers[i] * numbers[j]:
#                 answer = numbers[i] * numbers[j]
#     return answer

def solution(numbers):
    # numbers를 오름차순으로 정렬
    numbers.sort()
    
    # 가장 큰 두 수의 곱과 가장 작은 두 수의 곱 중 최댓값을 반환
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])