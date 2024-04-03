import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    N = int(input().rstrip())
    M = int(input().rstrip())
    vst = [-1] * (N+1)
    hst = [[] for _ in range(N+1)]
    arr = [[-1] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == -1:
            arr[a][b] = c
            hst[a].append(b)
        elif arr[a][b] > c:
            arr[a][b] = c
    s, e = map(int, input().rstrip().split())
    q = deque([(s, 0)])
    while q:
        n, cnt = q.popleft()
        if vst[n] == -1 or vst[n] == cnt:
            for i in hst[n]:
                temp = cnt + arr[n][i]
                if vst[i] == -1 or vst[i] > temp:
                    vst[i] = temp
                    if i != e:
                        q.append((i, temp))
    print(vst[e])
    return
solve()
