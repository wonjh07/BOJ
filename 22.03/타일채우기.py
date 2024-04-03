import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 31
dp[2] = 3
dp[4] = 11
new_block = 0
for i in range(6, N+1, 2):
    new_block += dp[i-4]
    dp[i] = dp[i-2] * 3 + new_block * 2 + 2
print(dp[N])