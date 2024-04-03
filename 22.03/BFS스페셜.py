import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = deque(list(map(int, input().split())))

#bfs
que = deque([1])
vst[1] = 1
ans.popleft()
while que:
    tmp = que.popleft()
    while ans:
        if ans[0] in arr[tmp] and not vst[ans[0]]:
            vst[ans[0]] = 1
            que.append(ans.popleft())
        else:
            break
    if not ans:
        break

if ans:
    print(0)
else:
    print(1)