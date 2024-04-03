import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def move(a, b, d, col):
    global sol
    while 1:
        tmp1, tmp2 = a + dy[d], b + dx[d]
        if arr[tmp1][tmp2] == '.':
            a, b = tmp1, tmp2
        elif arr[tmp1][tmp2] == 'O' and col == 'R':
            return -1, -1
        elif arr[tmp1][tmp2] == 'O' and col == 'B':
            return -1, -1
        else:
            return a, b

# 북 남 동 서
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
ri = rj = bi = bj = oi = oj = 0
arr = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            arr[i][j] = '.'
            ri, rj = i, j
        elif arr[i][j] == 'B':
            arr[i][j] = '.'
            bi, bj = i, j

sol = -1
que = deque([(1, ri, rj, bi, bj)])
while que:
    ln, ry, rx, by, bx = que.popleft()
    # 기울이는 횟수가 11번이면 que에서 제거
    if ln == 11:
        break
    for d in range(4):
        # 구슬을 차례차례로 일단 굴려보냄
        rty, rtx = move(ry, rx, d, 'R')
        bty, btx = move(by, bx, d, 'B')

        # 파란 구슬이 먼저 구멍에 빠진다면 해당방향은 생략
        if (bty == -1 and btx == -1):
            continue
        
        # 빨간 구슬만 빠졌다면 정답이므로 종료
        if (rty == -1 and rtx == -1):
            sol = ln
            break
        
        # 빨간 구슬, 파란구슬 위치가 중첩될때
        # 굴러 가는 방향 기준 앞에 있는 구슬이 먼저 도착하므로 뒷구슬은 뒤로 옮겨줌
        elif rty == bty and rtx == btx:
            if (d == 0 and ry < by) or (d == 1 and ry > by) or (d == 2 and rx > bx) or (d == 3 and rx < bx):
                bty, btx = bty - dy[d], btx - dx[d]
            else:
                rty, rtx = rty - dy[d], rtx - dx[d]
        
        # 굴러가고난 위치가 처음과 같다면 생략
        if [rty, rtx, bty, btx] == [ry, rx, by, bx]:
            continue
        
        que.append((ln+1, rty, rtx, bty, btx))

    if sol != -1:
        break 

print(sol)
