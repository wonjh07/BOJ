import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split(' '))
box = [[0] for _ in range(H)]
tomato = 0
ans = 0

q = deque([])
for h in range(H):
    box[h] = [[0] for _ in range(N)]
    for i in range(N):
        box[h][i] = list(map(int, input().rstrip().split(' ')))
        for j in range(M):
            if box[h][i][j] == 1:
                q.append((h, i, j, 1))
            if box[h][i][j] == 0:
                tomato += 1

while q and tomato:
    h, i, j, n = q.popleft()
    if ans < n:
        ans = n

    if (h > 0) and box[h-1][i][j] == 0:
        box[h-1][i][j] = 1
        q.append((h-1, i, j, n+1))
        tomato -= 1
    if (h < (H-1)) and box[h+1][i][j] == 0:
        box[h+1][i][j] = 1
        q.append((h+1, i, j, n+1))
        tomato -= 1
    if (i > 0) and box[h][i-1][j] == 0:
        box[h][i-1][j] = 1
        q.append((h, i-1, j, n+1))
        tomato -= 1
    if (i < (N-1)) and box[h][i+1][j] == 0:
        box[h][i+1][j] = 1
        q.append((h, i+1, j, n+1))
        tomato -= 1
    if (j > 0) and box[h][i][j-1] == 0:
        box[h][i][j-1] = 1
        q.append((h, i, j-1, n+1))
        tomato -= 1
    if (j < (M-1)) and box[h][i][j+1] == 0:
        box[h][i][j+1] = 1
        q.append((h, i, j+1, n+1))
        tomato -= 1

if tomato:
    print(-1)
else:
    print(ans)
