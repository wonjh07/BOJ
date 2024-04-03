import sys
input = sys.stdin.readline

def virus(area):
    global v_que, safe, sol
    test = [area[tt][:] for tt in range(N)]
    que = v_que[:]
    cnt = safe
    while que:
        y, x = que.pop(0)
        if y-1 >= 0 and test[y-1][x] == 0:
            test[y-1][x] = 2
            cnt -=1
            que.append([y-1, x])
        if y+1 < N and test[y+1][x] == 0:
            test[y+1][x] = 2
            cnt -=1
            que.append([y+1, x])
        if x-1 >= 0 and test[y][x-1] == 0:
            test[y][x-1] = 2
            cnt -=1
            que.append([y, x-1])
        if x+1 < M and test[y][x+1] == 0:
            test[y][x+1] = 2
            cnt -=1
            que.append([y, x+1])
    if sol < cnt-3:
        sol = cnt-3


def wall(ln, area, a, b):
    # 벽 3개 놓았으면 virus 실행
    if ln == 3:
        virus(area)
        return

    # 같은 행 a, b부터 검색
    for i in range(a, a+1):
        for j in range(b, M):
            if not area[i][j]:
                area[i][j] = 1
                wall(ln+1, area, i, j+1)
                area[i][j] = 0
                wall(ln, area, i, j+1)
                return

    # 다음행부터 전체 검색
    for i in range(a+1, N):
        for j in range(M):
            if not area[i][j]:
                area[i][j] = 1
                wall(ln+1, area, i, j+1)
                area[i][j] = 0
                wall(ln, area, i, j+1)
                return


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
v_que = []
safe = 0
sol = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 2:
            v_que.append([i, j])
        if lst[i][j] == 0:
            safe += 1
wall(0, lst, 0, 0)
print(sol)
