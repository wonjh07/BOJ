import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [x for x in lst]
for i in range(0, N):
    for j in range(0, i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))
