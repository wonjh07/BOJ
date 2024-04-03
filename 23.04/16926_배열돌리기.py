def solve():
    import sys
    sys.stdin = open("input.txt", "rt")
    input = sys.stdin.readline

    N, M, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    TOTAL = N * M
    cnt = 0
    i = 0
    while cnt < TOTAL:
        # 1. i번째 외곽의 갯수를 구해서 제자리로 돌아오는 만큼을 제외 시킨 나머지
        spin = R % ((N + M - (4 * i)) * 2 - 4)
        sy, sx = i, i
        stack = []
        # 2. i번쨰 외곽에 해당하는 요소들을 stack 에 저장
        for d in range(4):
            while 1:
                if d == 0 and sx == M - i - 1:
                    break
                elif d == 1 and sy == N - i - 1:
                    break
                elif d == 2 and sx == i:
                    break
                elif d == 3 and sy == i:
                    break
                stack.append(arr[sy][sx])
                sy, sx = sy + dy[d], sx + dx[d]
                cnt += 1

        # 3. 결과를 ans에 저장
        sy, sx = i, i
        j = spin
        size = len(stack)
        for d in range(4):
            while 1:
                if d == 0 and sx == M - i - 1:
                    break
                elif d == 1 and sy == N - i - 1:
                    break
                elif d == 2 and sx == i:
                    break
                elif d == 3 and sy == i:
                    break
                ans[sy][sx] = stack[j]
                sy, sx = sy + dy[d], sx + dx[d]
                j += 1
                if j == size:
                    j = 0
        i += 1
    
    for a in ans:
        print(*a, sep=" ")
    return

solve()


'''
정직하게 돌렸다가 실패한코드
나름 타겟만 미리 스핀돌려서 처리했는데도 오래걸림

def solve():
    import sys
    sys.stdin = open("input.txt", "rt")
    input = sys.stdin.readline

    N, M, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def get_target(y, x, spin, orbit, d):
        cnt = 0
        a, b = y, x
        while cnt < spin:
            while 1:
                if cnt == spin:
                    break
                if d == 0 and b == M - orbit - 1:
                    d = 1
                    break
                elif d == 1 and a == N - orbit - 1:
                    d = 2
                    break
                elif d == 2 and b == orbit:
                    d = 3
                    break
                elif d == 3 and a == orbit:
                    d = 0
                    break
                a, b = a + dy[d], b + dx[d]
                cnt += 1
        return a, b

    i = 0
    while 1:
        if ans[i][i]:
            break
        spin = R % ((N - (2 * i) - 1) * 4)
        sy, sx = i, i
        start = arr[i][i]
        ty, tx = get_target(i, i, spin, i, 0)
        for d in range(4):
            while 1:
                if ans[sy][sx]:
                    break
                if d == 0 and sx == M - i - 1:
                    break
                elif d == 1 and sy == N - i - 1:
                    break
                elif d == 2 and sx == i:
                    break
                elif d == 3 and sy == i:
                    break
                if ty == i and tx == i:
                    ans[sy][sx] = start
                else:
                    ans[sy][sx] = arr[ty][tx]
                sy, sx = sy + dy[d], sx + dx[d]
                ty, tx = get_target(sy, sx, spin, i, d)
        i += 1

    for a in ans:
        print(*a, sep=" ")
    return

solve()
'''