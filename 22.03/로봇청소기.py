'''
청소하는 영역의 개수

N x M 크기의 직사각형으로 나타낼 수 있으며, 
1 x 1 크기의 정사각형 칸으로 나누어져 있다.
각각의 칸은 벽 1 또는 빈 칸 0 이다. 
청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 
(r, c)

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    a.왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 
    b.그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    c.왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    d.네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 
바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

'''
import sys
input = sys.stdin.readline

def clean(r, c, d, cnt):
    global c_cnt
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    lx = [-1, 0, 1, 0]
    ly = [0, -1, 0, 1]

    drc = [3, 0, 1, 2] # 왼쪽돌려주는 것
    que = [[r, c, d, cnt]]
   
    while 1:
        Y, X, D, C = que.pop()
        if not lst[Y][X]:
            lst[Y][X] = 2
            c_cnt += 1
        # c, d
        if C == 4:
            if 0 <= Y + dy[D] < N and 0 <= X + dx[D] < M and lst[Y + dy[D]][X + dx[D]] == 2:
                que.append([Y + dy[D], X + dx[D], D, 0])
            else:
                lst[Y][X] = 3
                return
        # a, b
        else:
            if 0 <= Y + ly[D] < N and 0 <= X + lx[D] < M and not lst[Y + ly[D]][X + lx[D]]:
                que.append([Y + ly[D], X + lx[D], drc[D], 0])
            else:
                que.append([Y, X, drc[D], C+1])

N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
c_cnt = 0
clean(r, c, d, 0)
print(c_cnt)
