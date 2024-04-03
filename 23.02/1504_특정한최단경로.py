import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = float('inf')

#548ms heapq 사용으로 시간 단축
def bfs(N, s, way, arr, t1, t2):
    vst = [INF] * (N+1)
    vst[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        n, s = heapq.heappop(q)
        for i in way[s]:
            temp = n + arr[s][i]
            if vst[i] > temp:
                vst[i] = temp
                heapq.heappush(q, (temp, i))
    return vst[t1], vst[t2]

def main():
    N, E =  map(int, input().rstrip().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    way = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == 0:
            way[a].append(b)
            way[b].append(a)
        if arr[a][b] == 0 or arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    v1, v2 = map(int, input().rstrip().split())
    w1, w2 = bfs(N, 1, way, arr, v1, v2)
    w3, w4 = bfs(N, v1, way, arr, v2, N)
    w5, w6 = bfs(N, v2, way, arr, v1, N)

    res1 = w1 + w3 + w6
    res2 = w2 + w5 + w4

    res = min(res1, res2)
    if res >= INF:
        print(-1)
    else:
        print(res)
    return

main()



'''
import sys, time
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = float('inf')

# 904ms BFS 세번으로 최소화
def bfs(N, s, way, arr, t1, t2):
    vst = [INF] * (N+1)
    vst[s] = 0
    q = deque([(s, 0)])
    while q:
        s, n = q.popleft()
        for i in way[s]:
            temp = n + arr[s][i]
            if vst[i] > temp:
                vst[i] = temp
                q.append((i, temp))
    return vst[t1], vst[t2]

def main():
    N, E =  map(int, input().rstrip().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    way = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == 0:
            way[a].append(b)
            way[b].append(a)
        if arr[a][b] == 0 or arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    v1, v2 = map(int, input().rstrip().split())
    w1, w2 = bfs(N, 1, way, arr, v1, v2)
    w3, w4 = bfs(N, v1, way, arr, v2, N)
    w5, w6 = bfs(N, v2, way, arr, v1, N)

    res1 = w1 + w3 + w6
    res2 = w2 + w5 + w4

    res = min(res1, res2)
    if res == INF:
        print(-1)
    else:
        print(res)
    return
start = time.time()
main()
print(time.time()-start)

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = float('inf')

# 1368ms 반드시 v1, v2 포함 하는 분리 bfs
def bfs(N, s, e, way, arr):
    vst = [INF] * (N+1)
    q = deque([(s, 0)])
    if s == e:
        return 0
    while q:
        s, n = q.popleft()
        for i in way[s]:
            temp = n + arr[s][i]
            if vst[i] > temp:
                vst[i] = temp
                if i != e:
                    q.append((i, temp))
    return vst[e]

def main():
    N, E =  map(int, input().rstrip().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    way = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == 0:
            way[a].append(b)
            way[b].append(a)
            arr[a][b] = c
            arr[b][a] = c
        elif arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    v1, v2 = map(int, input().rstrip().split())
    bridge = bfs(N, v1, v2, way, arr)
    way1 = bfs(N, 1, v1, way, arr) + bfs(N, v2, N, way, arr)
    way2 = bfs(N, 1, v2, way, arr) + bfs(N, v1, N, way, arr)
    res = bridge + min(way1, way2)
    if res == INF:
        print(-1)
    else:
        print(res)
    return
main()

# 2888ms 느린 2차 vst 배열 버전 
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = float('inf')

def main():
    N, E =  map(int, input().rstrip().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    way = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == 0:
            way[a].append(b)
            way[b].append(a)
            arr[a][b] = c
            arr[b][a] = c
        elif arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    v1, v2 = map(int, input().rstrip().split())
    vst = [[INF] * (N+1) for _ in range(4)]
    start = 0
    if v1 == 1 and v2 == N:
        start = 3
    elif v1 == 1:
        start = 1
    elif v2 == N:
        start = 2

    q = deque([(1, 0, start)])
    while q:
        s, n, v = q.popleft()
        for i in way[s]:
            temp = n + arr[s][i]
            if vst[v][i] > temp:
                vst[v][i] = temp
                vt = v
                if v == 0 and i == v1:
                    vt = 1
                elif v == 0 and i == v2:
                    vt = 2
                elif (v == 1 and i == v2) or (v == 2 and i == v1):
                    vt = 3
                if not (v == 3 and i == N):
                    q.append((i, temp, vt))
    if vst[3][N] == INF:
        print(-1)
    else:
        print(vst[3][N])
    return
main()

'''

