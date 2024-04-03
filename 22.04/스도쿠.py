import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(st):
    global length, sol
    if st == length:
        sol = 1
        return
    a, b = blank[st]
    tmp = 3 * (a//3) + b//3
    for i in range(1, 10):
        if not vst1[a][i] and not vst2[b][i] and not vst3[tmp][i]:
            vst1[a][i] = 1
            vst2[b][i] = 1
            vst3[tmp][i] = 1
            arr[a][b] = i
            dfs(st+1)
            vst1[a][i] = 0
            vst2[b][i] = 0
            vst3[tmp][i] = 0
            if sol:
                return


arr = [list(map(int, input().rstrip())) for _ in range(9)]
blank = []
sol = 0
vst1 = [[0] * 10 for _ in range(10)]
vst2 = [[0] * 10 for _ in range(10)]
vst3 = [[0] * 10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j]:
            tmp = 3 * (i//3) + j//3
            vst1[i][arr[i][j]] = 1
            vst2[j][arr[i][j]] = 1
            vst3[tmp][arr[i][j]] = 1
        else:
            blank.append([i, j])
length = len(blank)
dfs(0)
for ans in arr:
    print(*ans, sep='')
