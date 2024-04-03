import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def move(t, x, d):
    vstz = [[0] * N for _ in range(N)]
    if d == 0 or d == 1:
        end = range(N)
    else:
        end = range(N-1, -1, -1)

    vst[t] = [vst[x][k][:] for k in range(N)]

    for i in end:
        for j in end:
            if vst[t][i][j]:
                a, b = i, j
                while 1:
                    ta, tb = a + dy[d], b + dx[d]
                    if 0 <= ta < N-1 and 0 <= tb < N-1:
                        if not vst[t][a][b]:
                            a, b = ta, tb
                        else:
                            if vst[t][a][b] == vst[t][i][j] and not vstz[a][b]:
                                vstz[a][b] = 1
                                vst[t][a][b] += vst[t][i][j]
                                vst[t][i][j] = 0
                            else:
                                if a != i and b != j:
                                    vst[t][ta][tb] = vst[t][i][j]
                                    vst[t][i][j] = 0
                                break
                    else:
                        if a != i and b != j:
                            vst[t][a][b] = vst[t][i][j]
                            vst[t][i][j] = 0
                        break
    return 


def search(x):
    global sol
    mx = 0
    for i in range(N):
        for j in range(N):
            if mx < vst[x][i][j]:
                mx = vst[x][i][j]
    if sol < mx:
        sol = mx

    
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
vst = [[[0] * N for _ in range(N)] for _ in range(4**5)]
vst[0] = arr
sol = 0


que = deque([(1, 0)])
while que:
    ln, x = que.popleft()
    search(x)
    t = x
    if ln < 6:
        for d in range(4):
            t += 1
            move(t, x, d)
            que.append((ln+1, t))

print(sol)
