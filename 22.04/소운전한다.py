import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = float('inf')
mx = 1000000000
V, E = map(int, input().split())
lst = [[] for _ in range(V+1)]
lst2 = [[] for _ in range(V+1)]
vst = [INF for _ in range(V+1)]
vst2 = [INF for _ in range(V+1)]

for _ in range(E):
    x, y, d, p = map(int, input().split())
    lst[x].append((y, d))
    lst[y].append((x, d))
    lst[x].append((-y, d-p))
    lst[y].append((-x, d-p))

que = []
que2 = []
heapq.heappush(que, (0, 1))
vst[1] = 0

while que:
    ssm, x = heapq.heappop(que)
    for e, d in lst[x]:
        if e < 0:
            e *= -1
            tmp = ssm + d
            if vst2[e] > tmp:
                vst2[e] = tmp
                heapq.heappush(que2, (tmp, e))
        else:
            tmp = ssm + d
            if vst[e] > tmp:
                vst[e] = tmp
                heapq.heappush(que, (tmp, e))

while que2:
    ssm, x = heapq.heappop(que2)
    for e, d in lst[x]:
        if e > 0:
            tmp = ssm + d
            if vst2[e] > tmp:
                vst2[e] = tmp
                heapq.heappush(que2, (tmp, e))

for k in range(2, V+1):
    print(vst2[k])
print(vst2)
