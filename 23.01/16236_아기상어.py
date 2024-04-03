import sys, time
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())
y, x = 0, 0
arr = [[0] * N for _ in range(N)]
fish = 0
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
size = 2
ate = 0
cnt = 0

for i in range(N):
    arr[i] = list(map(int, input().rstrip().split()))
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            y, x = i, j
        elif 1 <= arr[i][j] < 9:
            fish += 1

while 1:
    vst = [[0] * N for _ in range(N)]
    vst[y][x] = 1
    q = deque([(y, x, 0)])
    temp = []
    renew = False
    lmt = -1
    while q:
        yy, xx, n = q.popleft()
        if lmt != -1 and lmt < n:
            break
        for i in range(4):
            a, b = yy + dy[i], xx + dx[i]
            if 0 <= a < N and 0 <= b < N and not vst[a][b]:
                if size > arr[a][b] > 0:
                    temp.append((a, b, n+1))
                    lmt = n

                elif not temp and (arr[a][b] == 0 or size == arr[a][b]):
                    vst[a][b] = 1
                    q.append((a, b, n+1))

    if temp:
        temp.sort()
        y, x = temp[0][0], temp[0][1]
        arr[y][x] = 0
        cnt += temp[0][2]
        ate += 1
        if size == ate:
            size += 1
            ate = 0
        fish -= 1
        renew = True

    if not fish or not renew:
        break

print(cnt)
