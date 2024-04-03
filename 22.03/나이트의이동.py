import sys
input = sys.stdin.readline

def bfs(Y, X, ln):
    que = [[Y, X, ln]]
    while que:
        i, j, ln = que.pop(0)
        if i == A and j == B:
            print(ln)
            return
        for d in range(8):
            if (0 <= i+dy[d] < N and 0 <= j+dx[d] < N) and vst[i+dy[d]][j+dx[d]]:
                vst[i+dy[d]][j+dx[d]] = 0
                que.append([i+dy[d], j+dx[d], ln+1])


T = int(input())
for tc in range(T):
    N = int(input())
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    Y, X = map(int, input().split())
    A, B = map(int, input().split())
    vst = [[1] * N for _ in range(N)]
    vst[Y][X] = 0
    bfs(Y, X, 0)