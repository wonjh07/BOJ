import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

p_hq = []
n_hq = []
N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x > 0:
        heapq.heappush(p_hq, x)
    elif x < 0:
        heapq.heappush(n_hq, -x)

    elif x == 0:
        if not p_hq and not n_hq:
            print(0)
        elif p_hq and not n_hq:
            print(heapq.heappop(p_hq))
        elif (not p_hq and n_hq):
            print(-heapq.heappop(n_hq))
        else:
            if (p_hq[0] < n_hq[0]):
                print(heapq.heappop(p_hq))
            else:
                print(heapq.heappop(n_hq))