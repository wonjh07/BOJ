import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)


# dfs 로 순환선 구하기
def dfs(st, ln):
    global que
    for j in arr[st]:
        if vst[j] and ln - vst[j] >= 2:
            for y in stk[vst[j]-1:]:
                dis[y] = 0
                que.append([y, 0])
            return
        if not vst[j]:
            vst[j] = ln+1
            stk.append(j)
            dfs(j, ln+1)
            stk.pop()
        if que:
            return


N = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
dis = [-1] * (N+1)
stk = []
que = deque()

for _ in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N+1):
    if not vst[i]:
        vst[i] = 1
        stk = [i]
        dfs(i, 1)
    if que:
        break

# bfs
while que:
    sta, ln = que.popleft()
    for nxt in arr[sta]:
        if dis[nxt] == -1:
            dis[nxt] = ln+1
            que.append([nxt, ln+1])
print(*dis[1:])
