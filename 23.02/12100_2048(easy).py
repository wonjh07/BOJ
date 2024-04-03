import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    N = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = [0]

    def move(n, puzzle, cnt):
        if n == 5:
            if ans[0] < cnt:
                ans[0] = cnt
            return

        # 상
        temp = [[0] * N for _ in range(N)]
        mx = 0
        for j in range(N):
            cur = 0
            prv = 0
            for i in range(N):
                if puzzle[i][j]:
                    if prv == 0:
                        prv = puzzle[i][j]
                    elif prv == puzzle[i][j]:
                        temp[cur][j], prv = prv * 2, 0
                        if mx < temp[cur][j]:
                            mx = temp[cur][j]
                        cur += 1
                    else:
                        temp[cur][j], prv = prv, puzzle[i][j]
                        if mx < temp[cur][j]:
                            mx = temp[cur][j]
                        cur += 1
            if prv:
                temp[cur][j] = prv
                if mx < temp[cur][j]:
                    mx = temp[cur][j]
        move(n+1, temp, mx)
        
        # 하
        temp = [[0] * N for _ in range(N)]
        mx = 0
        for j in range(N):
            cur = N-1
            prv = 0
            for i in range(N-1, -1, -1):
                if puzzle[i][j]:
                    if prv == 0:
                        prv = puzzle[i][j]
                    elif prv == puzzle[i][j]:
                        temp[cur][j], prv = prv * 2, 0
                        if mx < temp[cur][j]:
                            mx = temp[cur][j]
                        cur -= 1
                    else:
                        temp[cur][j], prv = prv, puzzle[i][j]
                        if mx < temp[cur][j]:
                            mx = temp[cur][j]
                        cur -= 1
            if prv:
                temp[cur][j] = prv
                if mx < temp[cur][j]:
                    mx = temp[cur][j]
        move(n+1, temp, mx)

        # 좌
        temp = [[0] * N for _ in range(N)]
        mx = 0
        for i in range(N):
            cur = 0
            prv = 0
            for j in range(N):
                if puzzle[i][j]:
                    if prv == 0:
                        prv = puzzle[i][j]
                    elif prv == puzzle[i][j]:
                        temp[i][cur], prv = prv * 2, 0
                        if mx < temp[i][cur]:
                            mx = temp[i][cur]
                        cur += 1
                    else:
                        temp[i][cur], prv = prv, puzzle[i][j]
                        if mx < temp[i][cur]:
                            mx = temp[i][cur]
                        cur += 1
            if prv:
                temp[i][cur] = prv
                if mx < temp[cur][j]:
                    mx = temp[cur][j]
        move(n+1, temp, mx)

        # 우
        temp = [[0] * N for _ in range(N)]
        mx = 0
        for i in range(N):
            cur = N-1
            prv = 0
            for j in range(N-1, -1, -1):
                if puzzle[i][j]:
                    if prv == 0:
                        prv = puzzle[i][j]
                    elif prv == puzzle[i][j]:
                        temp[i][cur], prv = prv * 2, 0
                        if mx < temp[i][cur]:
                            mx = temp[i][cur]
                        cur -= 1
                    else:
                        temp[i][cur], prv = prv, puzzle[i][j]
                        if mx < temp[i][cur]:
                            mx = temp[i][cur]
                        cur -= 1
            if prv:
                temp[i][cur] = prv
                if mx < temp[cur][j]:
                    mx = temp[cur][j]
        move(n+1, temp, mx)
        return
    
    move(0, puzzle, 0)
    print(ans[0])
    return
solution()
