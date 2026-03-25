N = int(input())
words = set(input() for x in range(N))
words = list(words)
words.sort(key= lambda x: (len(x), x))

for w in words:
    print(w)