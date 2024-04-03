import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    dp = [[0] * N for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if i == j:
                dp[i][j] = 1
            elif nums[i] == nums[j]:
                if i + 1 == j or (dp[i+1][i+1] == 1 and dp[i+1][j-1] == 1):
                    dp[i][j] = 1
    for _ in range(M):
        s, e = map(int, input().rstrip().split())
        print(dp[s-1][e-1])

main()