def enemyfind(X, Y, board, D):
    # bfs 로 사거리내 가장 가까운 왼쪽 적 찾기
    # 궁수의 앞칸부터 시작하여 왼쪽 위 오른쪽 순으로 탐색
    vst = [[0] * M for _ in range(N+1)]
    que = [[X, Y, 1]]
    while 1:
        x, y, ln = que.pop(0)
        vst[x][y] = 1
        if ln > D:
            return -1, -1
        if board[x][y] == 1 or board[x][y] == -1:
            return x, y
        else:
            if y-1 >= 0 and not vst[x][y-1]:
                que.append([x, y-1, ln + 1])
            if x-1 > 0 and not vst[x-1][y]:
                que.append([x-1, y, ln + 1])
            if y+1 < M and not vst[x][y+1]:
                que.append([x, y+1, ln + 1])
    

def defense(cb, mst):
    global sol, N, M, D
    board = [cb[x][:] for x in range(N)] + [vst[:]]
    cnt = N+1
    kill = 0

    #프로그램 시작
    while cnt > 0:  # 공격 페이즈
        for i in range(M):  # 궁수 체크
            if board[N][i] == 2:  # 사거리 체크
                a, b = enemyfind(N-1, i, board, D)
                if a != -1 and b != -1:
                    if board[a][b] == 1:
                        board[a][b] = -1  # 이미제거된 적을 -1로 표기 (동시에 적 공격)
                        mst -= 1
                        kill += 1
        # 성 근처 적이동
        for i in range(M):
            if board[N-1][i] == 1 or board[N-1][i] == -1: 
                if board[N-1][i] == -1:
                    board[N-1][i] = 0
                elif board[N][i] == 2 or board[N][i] == 0:
                    mst -= 1
                    board[N-1][i] = 0
        # 몬스터가 더이상 없다면 종료
        if mst == 0:
            break
        # 나머지 적들 이동
        board = [board.pop(N-1)] + board
        # 맵에서 -1 제거
        for i in range(N):
            for j in range(M):
                if board[i][j] == -1:
                    board[i][j] = 0
        cnt -= 1

    # 현재 킬수 갱신
    if sol < kill:
        sol = kill
    return

# dfs로 성에 궁수 배치
def castling(st, ln, mst):
    global arr
    if st == M:
        if ln == 3:
            defense(arr, mst)  # 세명이 배치되고나면 디펜스 시작
        return
    vst[st] = 2  # 1은 몬스터, 2를 궁수로 세팅
    castling(st+1, ln+1, mst)
    vst[st] = 0
    castling(st+1, ln, mst)
    return


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
monster = 0
sol = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            monster += 1
vst = [0] * M
castling(0, 0, monster)
print(sol)