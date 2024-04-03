import sys
input = sys.stdin.readline
from collections import deque

def dfs(st):
    for i in arr[st]:
        if not vst[i]:
            vst[i] = 1
            root[st].append(i)
            dfs(i)


N = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
root = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = deque(list(map(int, input().split())))
vst[1] = 1
dfs(1)

ans.popleft()
stk = [1]
while stk:
    if not ans:
        break

    if root[stk[-1]]:
        lbl = 0
        for i in root[stk[-1]]:
            if i == ans[0]:
                root[stk[-1]].remove(i)
                ans.popleft()
                stk.append(i)
                lbl = 1
                break
        if not lbl:
            break
    else:
        stk.pop()

if ans:
    print(0)
else:
    print(1)
