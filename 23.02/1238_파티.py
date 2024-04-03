import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 56ms 다익스트라 반대간선이용해 최소찾기 
def main():
    N, M, X = map(int, input().rstrip().split())
    X -= 1
    INF = float('inf')
    arr1 = [[] for _ in range(N)]
    arr2 = [[] for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, input().rstrip().split())
        s, e = s - 1, e - 1
        arr1[s].append((t, e))
        arr2[e].append((t, s))

    def dijkstra(arr):
        q = [(0, X)]
        d = [INF] * N
        vst = [0] * N
        d[X] = 0
        while q:
            t1, s = heapq.heappop(q)
            if not vst[s]:
                vst[s] = 1
                for t2, e in arr[s]:
                    tmp = t1 + t2
                    if d[e] > tmp:
                        d[e] = tmp
                        heapq.heappush(q, (tmp, e))
        return d

    print(max(map(sum, zip(dijkstra(arr1), dijkstra(arr2)))))
    return

main()


'''
import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

#1024ms bfs 다익스트라
def main():
    N, M, X = map(int, input().rstrip().split())
    INF = float('inf')
    arr = [[] for _ in range(N)]
    vst = [[INF] * N for _ in range(N)]
    ans = 0
    for _ in range(M):
        s, e, t = map(int, input().rstrip().split())
        s, e = s - 1, e - 1
        arr[s].append((e, t))

    for r in range(N):
        q = []
        heapq.heappush(q, (0, r))
        vst[r][r] = 0
        while q:
            t, s = heapq.heappop(q)
            if vst[r][s] >= t:
                for e, d in arr[s]:
                    tmp = t + d
                    if vst[r][e] > tmp:
                        vst[r][e] = tmp
                        if e != X-1:
                            heapq.heappush(q, (tmp, e))
    for i in range(N):
        if i != X-1:
            temp = vst[i][X-1] + vst[X-1][i]
            if ans < temp:
                ans = temp
    print(ans)
    return

main()

시간초과 반복문 다익스트라
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N, M, X = map(int, input().rstrip().split())
    INF = float('inf')
    arr = [[] for _ in range(N)]
    ans = [0] * N

    for _ in range(M):
        s, e, t = map(int, input().rstrip().split())
        s, e = s - 1, e - 1
        arr[s].append((e, t))

    def dijkstra(i):
        d = [INF] * N
        vst = [0] * N
        d[i] = 0

        for _ in range(N):
            mn = INF
            mn_i = -1
            for j in range(N):
                if not vst[j] and d[j] < mn:
                    mn = d[j]
                    mn_i = j
            if mn_i == -1:
                break
            vst[mn_i] = 1
            for e, t in arr[mn_i]:
                d[e] = min(d[e], d[mn_i] + t)
        if i == X-1:
            for k in range(N):
                ans[k] += d[k]
        else:
            ans[i] += d[X-1]
        return

    for i in range(N):
        dijkstra(i)

    print(max(ans))
    return

main()

'''