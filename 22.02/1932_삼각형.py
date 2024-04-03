import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * i for i in range(1,501)]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if j == 0:
            dp[i][j] = lst[j]+dp[i-1][j]
        elif i == j:
            dp[i][j] = lst[j]+dp[i-1][j-1]
        else:
            dp[i][j] = max(lst[j]+dp[i-1][j], lst[j]+dp[i-1][j-1])
print(max(dp[N-1]))