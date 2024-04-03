def solve():
    import sys
    from collections import deque
    sys.stdin = open("input.txt", "rt")
    input = sys.stdin.readline

    INF = float("inf")
    R, C = map(int, input().split(' '))
    arr = [list(input().rstrip()) for _ in range(R)]
    vst = [[INF] * C for _ in range(R)]
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    ey, ex = 0, 0
    sy, sx = 0, 0
    wq = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                wq.append((i, j))
            if arr[i][j] == "D":
                ey, ex = i, j
            if arr[i][j] == "S":
                sy, sx = i, j

    vst[sy][sx] = 0
    sq = deque([(sy, sx, 1)])
    now = 0

    def water():
        temp = []
        for y, x in wq:
            for d in range(4):
                a, b = y + dy[d], x + dx[d]
                if 0 <= a < R and 0 <= b < C and arr[a][b] == ".":
                    arr[a][b] = "*"
                    temp.append((a, b))
        return temp
    
    # 1. 고슴도치 이동하기
    while sq:
        y, x, cnt = sq.popleft()
        # 2. 같은 시간내 고슴도치의 움직임 이후 물이 퍼짐
        if now != cnt:
            now = cnt
            wq = water()
            
        for d in range(4):
            a, b = y + dy[d], x + dx[d]
            if 0 <= a < R and 0 <= b < C and vst[a][b] > cnt:
                if arr[a][b] == "D":
                    return cnt
                elif arr[a][b] == ".":
                    vst[a][b] = cnt
                    sq.append((a, b, cnt + 1))

    return "KAKTUS"

print(solve())