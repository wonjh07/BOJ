import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x, n, ln):
    global sol
    for d in range(4):
        a, b = y+dy[d], x+dx[d]
        if 0 <= a < N and 0 <= b < M and vst[a][b] and arr[a][b] == n:
            if (ln - vst[a][b]) >= 3:
                sol = 1
                return
        if 0 <= a < N and 0 <= b < M and not vst[a][b] and arr[a][b] == n:
            vst[a][b] = ln+1
            dfs(a, b, n, ln+1)
        if sol:
            return


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
vst = [[0] * M for _ in range(N)]
sol = 0
for i in range(N):
    for j in range(M):
        if not vst[i][j]:
            vst[i][j] = 1
            dfs(i, j, arr[i][j], 1)
        if sol:
            break
    if sol:
        break
if sol:
    print('Yes')
else:
    print('No')
