import sys
from itertools import combinations
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 180ms 브루트포스
def main():
    N, M =  map(int, input().rstrip().split())
    INF = float("inf")
    chicken = []
    house = []
    ans = INF

    for i in range(N):
        arr = input().rstrip().split()
        for j in range(N):
            if arr[j] == '1':
                house.append((i, j))
            elif arr[j] == '2':
                chicken.append((i, j))

    for picks in combinations(chicken, M):
        res = 0
        for hi, hj in house:
            cnt = INF
            for pi, pj in picks:
                temp = abs(hi-pi) + abs(hj-pj)
                if cnt > temp:
                    cnt = temp
            res += cnt
        if ans > res:
            ans = res
    print(ans)
    return
main()

'''
3444ms bfs 활용 코드

import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve(N, pick, house, arr, mn):
    vst = [[0] * N for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q = deque(pick[::])
    cnt = 0
    value = 0
    while q:
        y, x, d = q.popleft()
        vst[y][x] = 1
        for k in range(4):
            y2, x2 = dy[k] + y, dx[k] + x
            if 0 <= y2 < N and 0 <= x2 < N and vst[y2][x2] == 0:
                if arr[y2][x2] == 1:
                    cnt += 1
                    value += d
                vst[y2][x2] = 1
                q.append((y2, x2, d+1))
            if value > mn[0]:
                return
            if house == cnt:
                if mn[0] > value:
                    mn[0] = value
                return

    return

def pick_chick(pick, n, idx, c, M, N, chick, house, arr, mn):
    if n == M:
        solve(N, pick, house, arr, mn)
        return
    for chi in range(idx, c):
        pick.append(chick[chi])
        pick_chick(pick, n+1, chi+1, c, M, N, chick, house, arr, mn)
        pick.pop(-1)
    return

def main():
    N, M =  map(int, input().rstrip().split())
    arr = [[] for _ in range(N)]
    chick = []
    house = 0
    mn = [1e13]
    for i in range(N):
        arr[i] = list(map(int, input().rstrip().split()))
        for j in range(N):
            if arr[i][j] == 2:
                chick.append((i, j, 1))
            elif arr[i][j] == 1:
                house += 1
    pick = []
    pick_chick(pick, 0, 0, len(chick), M, N, chick, house, arr, mn)
    print(mn[0])
    return

main()
'''