import sys
sys.stdin = open("input.txt", "r")


def dfs(y, x, ln):
    global mx, sol, cnt
    for d in range(4):
        a, b = y + dy[d], x + dx[d]
        if 0 <= a < N and 0 <= b < M and not vst[arr[a][b]]:
            vst[arr[a][b]] = 1
            dfs(a, b, ln+1)
            if sol:
                return
            vst[arr[a][b]] = 0
    else:
        if ln == cnt:
            mx = cnt
            sol = 1
            return
        if mx < ln:
            mx = ln


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
vst = [0] * 26
cnt = 0
for i in range(N):
    for j in range(M):
        arr[i][j] = ord(arr[i][j]) - 65
        if not vst[arr[i][j]]:
            vst[arr[i][j]] = 1
            cnt += 1
vst = [0] * 26
mx = 1
sol = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
vst[arr[0][0]] = 1
dfs(0, 0, 1)
print(mx)
