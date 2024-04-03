import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = float('inf')
mx = 1000000000
V, E = map(int, input().split())
lst = [[] for _ in range(2*V+2)]
vst = [INF for _ in range(2*V+2)]

for _ in range(E):
    x, y, d, p = map(int, input().split())
    lst[x].append((y, d))
    lst[y].append((x, d))
    lst[-x].append((-y, d))
    lst[-y].append((-x, d))
    lst[x].append((-y, mx+d-p))
    lst[y].append((-x, mx+d-p))

que = []
heapq.heappush(que, (0, 1))
vst[1] = 0
while que:
    ssm, x = heapq.heappop(que)
    for e, d in lst[x]:
        tmp = ssm + d
        if vst[e] > tmp:
            vst[e] = tmp
            heapq.heappush(que, (tmp, e))

for k in range(2, V+1):
    print(vst[-k]-mx)
print(vst)
