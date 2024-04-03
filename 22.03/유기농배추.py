import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(a, b):
    for d in range(4):
        if (0 <= a + dy[d] < N) and (0 <= b + dx[d] < M):
            if arr[a+dy[d]][b+dx[d]]:
                arr[a+dy[d]][b+dx[d]] = 0
                dfs(a+dy[d], b+dx[d])


T = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                arr[i][j] = 0
                dfs(i, j)
                cnt += 1
    print(cnt)
    