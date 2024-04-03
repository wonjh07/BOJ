import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
mx = 0
sts = [0] + [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N+1)]
dp[1] = [sts[1], 0]
if N > 1:
    dp[2] = [sts[1] + sts[2], sts[2]]
    for i in range(3, N+1):
        dp[i] = [sts[i]+dp[i-1][1], sts[i] + max(dp[i-2])]

print(max(dp[N]))