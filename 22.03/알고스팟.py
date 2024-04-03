import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
vst = [[-1] * M for _ in range(N)]
vst[0][0] = 0
mn = N*M
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
que = deque([[0, 0, 0]])
while que:
    i, j, ln = que.popleft()
    if (vst[i][j] == -1 or vst[i][j] == ln) and mn > ln:
        for d in range(4):
            a, b, k = i + dy[d], j + dx[d], ln
            if 0 <= a < N and 0 <= b < M:
                if arr[a][b]:
                    k += 1
                if vst[a][b] == -1 or vst[a][b] > k:
                    vst[a][b] = k
                    if a == N-1 and b == M-1:
                        if mn > ln:
                            mn = ln
                    else:
                        que.append([a, b, k])
print(vst[N-1][M-1])
