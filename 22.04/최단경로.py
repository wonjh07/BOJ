import heapq

N, M = map(int, input().split())
st = int(input())
lst = [[] for _ in range(N+1)]
vst = [-1] * (N+1)
vst[st] = 0
cnt = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
que = []
heapq.heappush(que, (0, st))

while que:
    ssm, x = heapq.heappop(que)
    if vst[x] < ssm:
        continue
    for i in lst[x]:
        tmp = ssm + i[1]
        if vst[i[0]] == -1 or vst[i[0]] > tmp:
            vst[i[0]] = tmp
            heapq.heappush(que, (tmp, i[0]))

for i in vst[1:]:
    if i == -1:
        print('INF')
    else:
        print(i)