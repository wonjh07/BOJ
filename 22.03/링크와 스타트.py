import sys
input = sys.stdin.readline


def f_start(st, ln, ssum):
    global mn
    # start 팀에 N-1명이 오면 중단 
    if ln == N-1:
        return

    # 그떄 그떄 마다 팀 스탯을 비교
    diff = abs(ssum - f_link())
    if mn > diff:
        mn = diff

    for i in range(st, N):
        if not vst[i]:
            # stk에 추가될때마다 팀원들간 능력치 더해주기
            tmp = 0
            for k in stk:
                tmp += T[i][k] + T[k][i]
            # 재귀
            vst[i] = 1
            stk.append(i)
            f_start(i+1, ln+1, ssum+tmp)
            vst[i] = 0
            stk.pop()


def f_link():
    # 상대팀 능력치합
    ssum2 = 0
    r_stk = []
    for j in range(N):
        if not vst[j]:
            if r_stk:
                for y in r_stk:
                    ssum2 += T[j][y] + T[y][j]
            r_stk.append(j)
    return ssum2


N = int(input())
T = [[] for _ in range(N)]
mn = float('inf')
vst = [0] * N
stk = []
for x in range(N):
    T[x] = list(map(int, input().split()))

# 첫번쨰 선수는 고정
vst[0] = 1
stk = [0]
f_start(1, 1, 0)
print(mn)