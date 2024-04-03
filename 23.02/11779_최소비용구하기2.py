import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 183ms 시간 파이썬 전체2등
def main():
    N = int(input().rstrip())
    M = int(input().rstrip())
    INF = float('inf')
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().rstrip().split())
        arr[a].append((b, c))
    s, e = map(int, input().rstrip().split())
    # 다익스트라
    vst = [0] * (N+1)
    dist = [INF] * (N+1)
    hst = [[] for _ in range(N+1)]
    dist[s] = 0 
    for _ in range(1, N+1):
        mn = INF
        mn_i = -1
        for j in range(1, N+1):
            if not vst[j] and dist[j] < mn:
                mn = dist[j]
                mn_i = j
        if mn_i == -1:
            break
        for a, b in arr[mn_i]:
            temp = dist[mn_i] + b
            if dist[a] > temp:
                dist[a] = temp
                hst[a] = hst[mn_i][:]
                hst[a].append(mn_i)
        vst[mn_i] = 1
    hst[e].append(e)
    print(dist[e])
    print(len(hst[e]))
    print(*hst[e])
    return

main()