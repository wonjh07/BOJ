import sys
input = sys.stdin.readline

lst = [0] * 10001
dp = [0] * 10001
cnt = 0
N = int(input())
for i in range(1, N+1):
    lst[i] = int(input())
    if i < 3:
        dp[i] = dp[i-1] + lst[i]
    if i >= 3:
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i], dp[i-1])

print(dp[N])