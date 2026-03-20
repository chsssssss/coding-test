a = list(input())
b = list(input())

result = 0
a_dic = {}
b_dic= {}

for i in a:
    if i in a_dic:
        a_dic[i] += 1
    else:
        a_dic[i] = 1

for j in b:
    if j in b_dic:
        b_dic[j] += 1
    else:
        b_dic[j] = 1


for key in set(a_dic) | set(b_dic):
    result += abs(a_dic.get(key, 0) - b_dic.get(key, 0))
print(result)