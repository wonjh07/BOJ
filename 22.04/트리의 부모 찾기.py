import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())
lst = [[] for _ in range(N+1)]
root = [[] for _ in range(N+1)]
vst = [0] * (N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

que = deque([1])
vst[1] = 1
while que:
    x = que.popleft()
    for nd in lst[x]:
        if not vst[nd]:
            vst[nd] = 1
            root[nd].append(x)
            que.append(nd)
for i in range(2, N+1):
    print(*root[i])
