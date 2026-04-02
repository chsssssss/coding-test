def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    result = dfs(begin, target, visited, words, 0)
    return 0 if result > len(words) else result

def dfs(word, target, visited, words, count):
    min_count = 10000
    if target == word:
        return count
    
    for idx in range(len(words)):
        cnt = 0
        if not visited[idx]:
            for i in range(len(words[idx])):
                if word[i] != words[idx][i]:
                    cnt += 1
            if cnt == 1:
                visited[idx] = True
                print(count, words[idx])
                res = dfs(words[idx], target, visited, words, count + 1)
                min_count = min(res, min_count)
                visited[idx] = False
    return min_count