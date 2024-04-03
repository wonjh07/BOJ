import sys
input = sys.stdin.readline

def visit(a, b, mod):
    vst[a][b] += mod
    if a > 0:
        vst[a-1][b] += mod
    if a < N-1:
        vst[a+1][b] += mod
    if b > 0:
        vst[a][b-1] += mod
    if b < M-1:
        vst[a][b+1] += mod


def dfs(stx, sty, ln, ssum):
    global mx
    if ln == K:
        if mx < ssum:
            mx = ssum
        return

    for i in range(stx, stx+1):
        for j in range(sty, M):
            if not vst[i][j]:
                visit(i, j, 1)
                dfs(i, j, ln+1, ssum+lst[i][j])
                visit(i, j, -1)

    for i in range(stx+1, N):
        for j in range(M):
            if not vst[i][j]:
                visit(i, j, 1)
                dfs(i, j, ln+1, ssum+lst[i][j])
                visit(i, j, -1)
    return


N, M, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
vst = [[0] * M for _ in range(N)]
mx = -float('inf')
dfs(0, 0, 0, 0)
print(mx)