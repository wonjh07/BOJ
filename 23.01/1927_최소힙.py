import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())
hq = []

for _ in range(N):
    line = int(input().rstrip())
    if line == 0 and len(hq) != 0:
        print(-heapq.heappop(hq))
    elif line == 0 and len(hq) == 0:
        print(0)
    elif line != 0:
        heapq.heappush(hq, -line)