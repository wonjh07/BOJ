#1404ms 
#리뷰: 치즈를 녹이는데 BFS, 시간이 지날때마다 내부공기와 바깥공기가 연결되어있는지 판별하는 DFS를 동시에 사용

import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    vst = [[0] * M for _ in range(N)]
    q = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j, 1))

    def air_flows(ri, rj, m):
        arr[ri][rj] = m
        for k in range(4):
            ra, rb = ri + dy[k], rj + dx[k]
            if 0 <= ra < N and 0 <= rb < M and m < arr[ra][rb] <= 0:
                air_flows(ra, rb, m)
        return

    res = 0
    while q:
        i, j, t = q.popleft()
        if res < t:
            res = t
            air_flows(0, 0, -t)
        cnt = 0
        for k in range(4):
            a, b = i + dy[k], j + dx[k]
            if 0 <= a < N and 0 <= b < M and arr[a][b] < 0 and vst[a][b] < t:
                cnt += 1
            if cnt == 2:
                vst[i][j] = t
                arr[i][j] = -t
                break
        if cnt < 2:
            q.append((i, j, t+1))
    print(t)
    return

main()
