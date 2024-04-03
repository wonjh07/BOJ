import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(a, b):
    global cnt
    lbl = 0
    for d in range(4):
        if (0 <= a + dy[d] < N) and (0 <= b + dx[d] < N) and arr[a+dy[d]][b+dx[d]] == 1:
            arr[a+dy[d]][b+dx[d]] = num
            dfs(a+dy[d], b+dx[d])
        elif (0 <= a + dy[d] < N) and (0 <= b + dx[d] < N) and not arr[a+dy[d]][b+dx[d]]:
            lbl = 1
    if lbl:
        que.append([a, b])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ln = [[0]*N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
que = deque()
sol = 0
num = -1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = num
            dfs(i, j)
            num -= 1

#bfs
while que:
    a, b = que.popleft()
    for d in range(4):
        if (0 <= a + dy[d] < N) and (0 <= b + dx[d] < N):
            if not arr[a+dy[d]][b+dx[d]]:
                arr[a+dy[d]][b+dx[d]] = arr[a][b]
                ln[a+dy[d]][b+dx[d]] = ln[a][b] + 1
                que.append([a+dy[d], b+dx[d]])
            elif arr[a][b] != arr[a+dy[d]][b+dx[d]]:
                sol = ln[a+dy[d]][b+dx[d]] + ln[a][b]
                break
    if sol:
        break

print(sol)
