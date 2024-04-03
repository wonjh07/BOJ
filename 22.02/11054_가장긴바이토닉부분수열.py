import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
rv_lst = lst[::-1]
dp_len = [1] * N
dp_rv_len = [1] * N
dp_tot_len = [1] * N
dp = [[x] for x in lst]
dp_rv = [[x] for x in lst]
for i in range(N):
    for j in range(i):
        if rv_lst[j] < rv_lst[i] and dp_rv_len[i] <= dp_rv_len[j]:
            dp_rv_len[i] = dp_rv_len[j] + 1
            dp_rv[i] = dp_rv[j] + [rv_lst[i]]

        if lst[j] < lst[i] and dp_len[i] <= dp_len[j]:
            dp_len[i] = dp_len[j] + 1
            dp[i] = dp[j] + [lst[i]]
for i in range(N):
    dp_tot_len[i] =  dp_len[i] + dp_rv_len[N-1-i] - 1
print(max(dp_tot_len))
