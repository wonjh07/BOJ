import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 2
    arr[0] = list(map(int, input().split()))
    arr[1] = list(map(int, input().split()))

    dp = [[arr[0][0], arr[1][0]]]

    for i in range(1, N):
        a = max(dp[i-1][1] + arr[0][i], dp[i-1][0])
        b = max(dp[i-1][0] + arr[1][i], dp[i-1][1])
        dp.append([a, b])
    
    print(max(dp[N-1]))
