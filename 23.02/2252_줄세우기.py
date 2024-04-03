import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split())
    idg = [0] * (N+1)
    gph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().rstrip().split())
        idg[e] += 1
        gph[s].append(e)
    q = deque([i for i in range(1, N + 1) if idg[i] == 0])
    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nxt in gph[cur]:
            idg[nxt] -= 1
            if idg[nxt] == 0:
                q.append(nxt)
    print(*ans)
    return
main()