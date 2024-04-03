import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

arr = [0] * 101
dp = [0] * 101
N, M = map(int, input().rstrip().split(' '))
ans = 0

for _ in range(N):
    x, y = map(int, input().rstrip().split(' '))
    arr[x] = y

for _ in range(M):
    u, v = map(int, input().rstrip().split(' '))
    arr[u] = v

# 시작점을 0으로 잡는 실수를 했음
q = deque([(1, 1)])

while q:
    n, s = q.popleft()
    for i in range(s+6, s, -1):
        if i == 100:
                dp[i] = n
                ans = n
                break

        if i <= 100:
            if arr[i] and (dp[arr[i]] == 0 or n < dp[arr[i]]):
                dp[arr[i]] = n
                q.append((n+1, arr[i]))

            elif not arr[i] and (dp[i] == 0 or n < dp[i]):
                dp[i] = n
                q.append((n+1, i))

    if ans:
        break

print(ans)


'''
        if dp[i] == 0 or n < dp[i]:
            # 실수한 부분 arr[i] 로 가는 경우에는
            # dp[i]를 검사하면 안됬음
            # 선입 선출이기에 굳이 heapq가 필요없음
            if arr[i]:
                dp[arr[i]] = n
                heapq.heappush(hq, (n+1, arr[i]))
            else:
                dp[i] = n
                heapq.heappush(hq, (n+1, i))
'''
