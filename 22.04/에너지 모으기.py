import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
lst = list(map(int, input().split()))
que = []
mx = 0
heapq.heappush(que, (0, lst, N))
while que:
    ssum, bead, ln = heapq.heappop(que)
    if ln > 2:
        for i in range(1, ln-1):
            tp = bead[:]
            tmp = bead[i-1] * bead[i+1]
            tp.pop(i)
            heapq.heappush(que, (ssum - tmp, tp, ln-1))
    else:
        if mx > ssum:
            mx = ssum
            break

print(-mx)
