import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 3 for _ in range(1001)]
for k in range(1, N+1):
    R, G, B = map(int, input().split())
    dp[k][0] = min(dp[k-1][1],dp[k-1][2]) + R
    dp[k][1] = min(dp[k-1][0],dp[k-1][2]) + G
    dp[k][2] = min(dp[k-1][0],dp[k-1][1]) + B
print(min(dp[N]))