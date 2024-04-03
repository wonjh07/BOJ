import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
stk = [[] for _ in range(N+1)]
sol = 1
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = list(map(int, input().split()))

#bfs
q = deque([1])
vst[1] = 1
while q:
    x = q.popleft()
    for y in arr[x]:
        if not vst[y]:
            vst[y] = 1
            stk[x].append(y)
            q.append(y)


que = deque([1])
idx = 1
while que:
    a = stk[que.popleft()]
    b = ans[idx:idx+len(a)]
    if set(a) != set(b):
        sol = 0
        break
    que.extend(b)
    idx += len(a)

print(sol)
