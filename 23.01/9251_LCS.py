import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    a = input().rstrip()
    b = input().rstrip()
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-2][-2])
    return

solve()
