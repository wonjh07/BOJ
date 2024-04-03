import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(a, b):
    global cnt
    lbl = 0
    for d in range(4):
        if (0 <= a + dy[d] < N) and (0 <= b + dx[d] < N) and arr[a+dy[d]][b+dx[d]] == 1:
            arr[a+dy[d]][b+dx[d]] = -1
            dfs(a+dy[d], b+dx[d])
        elif (0 <= a + dy[d] < N) and (0 <= b + dx[d] < N) and not arr[a+dy[d]][b+dx[d]]:
            lbl = 1
    if lbl:
        tmp.append((a, b))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
lands = []
sol = 201
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            tmp = []
            arr[i][j] = -1
            dfs(i, j)
            lands.append(tmp)

for l1 in range(len(lands)):
    for l2 in range(l1+1, len(lands)):
        for q in lands[l1]:
            for w in lands[l2]:
                tmp = abs(q[0] - w[0]) +abs(q[1] - w[1])
                if sol > tmp:
                    sol = tmp

print(lands)
print(sol-1)
