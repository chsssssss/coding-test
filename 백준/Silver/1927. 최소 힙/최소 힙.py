import heapq
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
heap = []
output = []

for i in range(1, N + 1):
    a = int(data[i])
    if a == 0:
        if heap:
            output.append(str(heapq.heappop(heap)))
        else:
            output.append('0')
    else:
        heapq.heappush(heap, a)
print('\n'.join(output))