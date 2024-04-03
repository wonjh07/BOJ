import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(i, j, ln):
    global ans
    ti, tj = 0, 0
    if ln == 80:
        return
    if ln == 81:
        ans = [arr[end][1:] for end in range(1, 10)]
        return
    # 첫번째 지점부터 탐색해서 가장먼저 발견한 빈칸
    for sj in range(j, 10):
        if not arr[i][sj]:
            ti, tj = i, sj
            break
    else:
        for si in range(i+1, 10):
            for sj in range(1, 10):
                if not arr[si][sj]:
                    ti, tj = si, sj
                    break
            if ti and tj:
                break

    # 찾은 빈칸에 대해서 vst처리후 tmp구역값 처리
    tmp1 = 3 * ((ti-1)//3) + (tj-1)//3

    # 1. 칸에 들어갈수 있는 모든 숫자에 대해 dfs 실행
    # 2. 인접칸을 찾고 인접칸과 동시에 들어갈수 있는 숫자 찾기
    # 3. 숫자 쌍을 찾으면 vst에서 도미노쌍이 쓰인적없는지 확인후 다음 칸 dfs(ti, tj+1, ln+2) 실행

    #1.
    for k1 in range(1, 10):
        if not vst1[ti][k1] and not vst2[tj][k1] and not vst3[tmp1][k1]:
            #2.
            for d in range(2):
                a, b = ti + dy[d], tj + dx[d]
                if 1 <= a < 10 and 1 <= b < 10 and not arr[a][b]:
                    tmp2 = 3 * ((a-1)//3) + (b-1)//3
                    for k2 in range(1, 10):
                        if k1 != k2 and not vst1[a][k2] and not vst2[b][k2] and not vst3[tmp2][k2]:
                            #3.
                            if not vst[k1][k2]:
                                arr[ti][tj] = k1
                                arr[a][b] = k2
                                vst[k1][k2] = vst[k2][k1] = 1
                                vst1[ti][k1] = vst2[tj][k1] = vst3[tmp1][k1] = 1
                                vst1[a][k2] = vst2[b][k2] = vst3[tmp2][k2] = 1
                                dfs(ti, tj+1, ln+2)
                                if ans:
                                    return
                                arr[ti][tj] = 0
                                arr[a][b] = 0
                                vst[k1][k2] = vst[k2][k1] = 0
                                vst1[ti][k1] = vst2[tj][k1] = vst3[tmp1][k1] = 0
                                vst1[a][k2] = vst2[b][k2] = vst3[tmp2][k2] = 0


# main
tc = 1
while 1:
    N = int(input())
    if not N:
        break
    dx = [1, 0]
    dy = [0, 1]
    arr = [[0] * 10 for _ in range(10)]
    vst = [[0] * 10 for _ in range(10)]
    vst1 = [[0] * 10 for _ in range(10)]
    vst2 = [[0] * 10 for _ in range(10)]
    vst3 = [[0] * 10 for _ in range(9)]
    ans = []

    # vst 도미노 쌍 저장
    # check vst1: 가로, vst2: 세로, vs3: 정사각형구역
    # 도미노 갯수 받기
    for _ in range(N):
        a, ta, b, tb = input().rstrip().split()
        a, b = int(a), int(b)
        ta, tb = [ord(ta[0])-64, int(ta[1])], [ord(tb[0])-64, int(tb[1])]
        arr[ta[0]][ta[1]] = int(a)
        arr[tb[0]][tb[1]] = int(b)
        # 같은 도미노 쌍은 한개밖에 존재 하지않으므로 간선처럼 이어주기
        vst[a][b] = vst[b][a] = 1
        # vst1, vst2 가로 세로 check 처리
        vst1[ta[0]][a] = vst1[tb[0]][b] = 1
        vst2[ta[1]][a] = vst2[tb[1]][b] = 1
        # vst3 구역 찾기
        tmp1 = 3 * ((ta[0]-1)//3) + (ta[1]-1)//3
        tmp2 = 3 * ((tb[0]-1)//3) + (tb[1]-1)//3
        vst3[tmp1][a] = vst3[tmp2][b] = 1

    # 한 개인 arr 값 처리
    # 한개숫자는 도미노가아니므로 vst는 처리하지 않음
    lst = list(input().rstrip().split())
    for i in range(9, 0, -1):
        a, b = ord(lst[i-1][0])-64, int(lst[i-1][1])
        arr[a][b] = i
        tmp1 = 3 * ((a-1)//3) + (b-1)//3
        vst1[a][i] = vst2[b][i] = vst3[tmp1][i] = 1

    # ln 에 현재 채워진 칸수 전달
    dfs(1, 1, (N*2)+9)
    print(f'Puzzle {tc}')
    for x in ans:
        print(*x, sep='')
    tc += 1
