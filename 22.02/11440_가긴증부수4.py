import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[1, [i]] for i in lst]
cnt = 1
sol = [lst[0]]
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i] and dp[i][0] <= dp[j][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = dp[j][1] + [lst[i]]
            if cnt < dp[i][0]:
                cnt = dp[i][0]
                sol = dp[i][1]
print(cnt)
print(*sol)