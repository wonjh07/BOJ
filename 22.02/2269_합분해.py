'''
1 1 1 1 1 1 1 1 1 1 1 1 
1 2 3 4 5 6 7 8 9 10...
1 3 6 10 15 ...

dp[i][j] = sum(dp[i-1][:j+1])
'''

mod = 1000000000
N, K = map(int, input().split())
dp = [[0], [1 for _ in range(N+1)]] 
for i in range(2, K+1):
    tmp = []
    for j in range(N+1):
        tmp.append(sum(dp[i-1][:j+1]) % mod)
    dp.append(tmp)
print(dp[K][N] % mod)