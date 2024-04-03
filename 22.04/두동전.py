import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
coins = [0]
sol = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            coins.append([i, j])

que = deque([coins[:]])
while que:
    print(que)
    ln, c1, c2 = que.popleft()
    if ln == 10:
        break
    for d in range(4):
        cnt = 0
        y1, x1 = c1[0] + dy[d], c1[1] + dx[d]
        y2, x2 = c2[0] + dy[d], c2[1] + dx[d]
        if 0 <= y1 < N and 0 <= x1 < M:
            cnt += 1
        if 0 <= y2 < N and 0 <= x2 < M:
            cnt += 1
        if cnt == 1:
            sol = ln+1
            break
        if cnt == 2:
            if arr[y1][x1] != '#' or arr[y2][x2] != '#':
                if arr[y1][x1] == '#':
                    y1, x1 = c1[0], c1[1]
                if arr[y2][x2] == '#':
                    y2, x2 = c2[0], c2[1]
                que.append([ln+1, [y1, x1], [y2, x2]])
    if sol != -1:
        break
print(sol)