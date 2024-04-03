import sys
input = sys.stdin.readline

mod = 1000000009
dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    tmp = (dp[i-1] + dp[i-2] + dp[i-3]) % mod
    dp.append(tmp)
T = int(input())
for tc in range(1, T+1):
    ip = int(input())
    print(dp[ip])

'''
0 = [0, 0, 0]
1 = [1, 0, 0]
2 = [1, 1, 0]
3 = [2, 1, 1]
4 = [4, 2, 1]
5 = [7, 4, 2]
'''
