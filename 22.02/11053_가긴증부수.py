import sys
input = sys.stdin.readline

T = int(input())
lst = list(map(int, input().split()))
dp = [0] * 100
cnt = 0
for i in lst:
    for j in range(1,T+1):
        if i <= dp[j] or dp[j]==0:
            dp[j] = i
            if cnt < j:
                cnt = j
            break
print(cnt)
