import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 184ms bfs 탐색
def main():
    N, M, R = map(int, input().rstrip().split())
    value = list(map(int, input().rstrip().split()))
    cnt = [v for v in value]
    vst = [[0] * N for _ in range(N)]
    arr = [[] for _ in range(N)]
    for i in range(N):
        vst[i][i] = 1

    for _ in range(R):
        a, b, c = map(int, input().rstrip().split())
        if c <= M:
            a, b = a-1, b-1
            arr[a].append((b, c))
            arr[b].append((a, c))
    
    q = deque([(i, 0, i) for i in range(N)])

    while q:
        s, n, r = q.popleft()
        for i, dist in arr[s]:
            temp = n + dist
            if temp <= M:
                if not vst[r][i]:
                    cnt[r] += value[i]
                    vst[r][i] = 1
                q.append((i, temp, r))
    print(max(cnt))
    return

main()
'''
40ms 찐 다익스트라

def main():
    N, M, R = map(int, input().rstrip().split())
    value = list(map(int, input().rstrip().split()))
    arr = [[] for _ in range(N)]
    for _ in range(R):
        a, b, c = map(int, input().rstrip().split())
        if c <= M:
            a, b = a-1, b-1
            arr[a].append((c, b))
            arr[b].append((c, a))

    def dijkstra(i):
        d = [16] * N
        vst = [0] * N
        d[i] = 0
        res = 0

        for _ in range(N):
            mn = M + 1
            mn_idx = -1
            for j in range(N):
                if not vst[j] and d[j] < mn:
                    mn = d[j]
                    mn_idx = j
            if mn_idx == -1:
                break
            vst[mn_idx] = 1
            res += value[mn_idx]
            for s, n in arr[mn_idx]:
                d[n] = min(d[n], d[mn_idx] + s)

        return res

    ans = 0
    for i in range(N):
        ans = max(ans, dijkstra(i))
    print(ans)
    return

main()


256ms 플루이드 워셜 

def main():
    N, M, R = map(int, input().rstrip().split())
    value = list(map(int, input().rstrip().split()))
    arr = [[INF] * N for _ in range(N)]
    ans = 0

    for _ in range(R):
        a, b, c = map(int, input().rstrip().split())
        if c <= M:
            a, b = a-1, b-1
            arr[a][b] = c
            arr[b][a] = c

    for i in range(N):
        arr[i][i] = 0
        for j in range(N):
            if j != i:
                for k in range(N):
                    if k != i and k != j:
                        arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

    for i in range(N):
        res = 0
        for j in range(N):
            if arr[i][j] <= M:
                res += value[j]
        if ans < res:
            ans = res
    print(arr)
    print(ans)
    return

main()
'''