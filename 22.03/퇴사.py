import sys
input = sys.stdin.readline

N = int(input())
lst = [0, 0] * 15
dp = [0] * (N+1)
max_v = 0
for i in range(1, N+1):
    lst[i] = list(map(int, input().split()))

for j in range(N, 0, -1):
    if lst[j][0] > N - j + 1:
        dp[j] = 0
    else:
        dp[j] = lst[j][1]
        if j+(lst[j][0]) <= N:
            dp[j] += max(dp[j+(lst[j][0]):])

print(max(dp))
