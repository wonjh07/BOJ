import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
que = deque([])
cnt = N * M
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            que.append([i, j, 0])
            cnt -= 1
        elif lst[i][j] == -1:
            cnt -= 1
# bfs
while que:
        i, j, ln = que.popleft()
        for d in range(4):
            if (0 <= i+dy[d] < N and 0 <= j+dx[d] < M) and not lst[i+dy[d]][j+dx[d]]:
                lst[i+dy[d]][j+dx[d]] = 1
                cnt -= 1
                que.append([i+dy[d], j+dx[d], ln+1])
if cnt == 0:
    print(ln)
else:
    print(-1)
