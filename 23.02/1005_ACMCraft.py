import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 912ms DP + Que + 위상정렬
def main():
    T = int(input().rstrip())
    for _ in range(T):
        N, M = map(int, input().rstrip().split())
        cost = list(map(int, input().rstrip().split()))
        route = [[] for _ in range(N)]
        priority = [0] * N
        res = 0
        dp = [0] * N
        for _ in range(M):
            s, e = map(int, input().rstrip().split())
            s, e = s - 1, e - 1
            route[s].append(e)
            priority[e] += 1
        W = int(input().rstrip()) - 1

        q = deque([])
        for i in range(N):
            if priority[i] == 0:
                q.append(i)
                priority[i] = -1
        
        while q:
            i = q.popleft()
            c = cost[i] + dp[i]
            if i == W:
                res = c
                break
            for r in route[i]:
                priority[r] -= 1
                if priority[r] == 0:
                    q.append(r)
                    priority[r] = -1
                if dp[r] < c:
                    dp[r] = c
        print(res)
    return
main()


'''
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        N, M = map(int, input().split())
        time = list(map(int, input().split()))
        route = [[] for _ in range(N)]
        indegree = [0] * N
        dp = [0] * N

        for _ in range(M):
            a, b = map(int, input().split())
            route[a-1].append(b-1)
            indegree[b-1] += 1

        W = int(input()) - 1
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i]

        while q:
            idx = q.popleft()
            if idx == W:
                break
            for nxt in route[idx]:
                indegree[nxt] -= 1
                dp[nxt] = max(dp[nxt], dp[idx] + time[nxt])
                if indegree[nxt] == 0:
                    q.append(nxt)

        print(dp[W])
    return
main()
'''