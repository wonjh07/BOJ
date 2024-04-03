'''
10 30 10 20 20 10
dp[i]
30 10
30 20
30 20 10
'''

N = int(input())
lst = list(map(int, input().split()))
dp_len = [1] * N
dp = [[x] for x in lst]
for i in range(N):
    for j in range(i):
        if lst[j] > lst[i] and dp_len[i] <= dp_len[j]:
            dp_len[i] = dp_len[j] + 1
            dp[i] = dp[j] + [lst[i]]
print(max(dp_len))
