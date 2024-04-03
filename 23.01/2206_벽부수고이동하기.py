import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    N, M = map(int, input().rstrip().split())
    arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    vst = [[-1] * M for _ in range(N)]
    vst2 = [[-1] * M for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    vst[0][0], vst2[0][0] = 0, 0
    q = deque([(0, 0, 0, 0)])
    if N == 1 and M == 1:
        print(1)

    else:
        while q:
            y, x, c, w = q.popleft()
            c += 1
            for i in range(4):
                a, b, ww = y + dy[i], x + dx[i], w

                if 0 <= a < N and 0 <= b < M:
                    if arr[a][b] == 1 and w == 0:
                        ww += 1
                    elif arr[a][b] == 1 and w > 0:
                        continue

                    if (vst[a][b] == -1 or vst[a][b] > c) and ww == 0:
                        vst[a][b] = c
                        vst2[a][b] = c
                        q.append((a, b, c, ww))
                    elif (vst2[a][b] == -1 or vst2[a][b] > c) and ww == 1:
                        vst2[a][b] = c
                        q.append((a, b, c, ww))
                    
                if vst2[N-1][M-1] != -1:
                    vst2[N-1][M-1] += 1
                    break
            if vst2[N-1][M-1] != -1:
                    break
        print(vst2[N-1][M-1])
    return

solve()