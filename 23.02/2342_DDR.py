import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solution():
    INF = float('inf')
    arr = list(map(int, input().split()))
    cost = [[0, 2, 2, 2, 2], [0, 1, 3, 4, 3], [0, 3, 1, 3, 4], [0, 4, 3, 1, 3], [0, 3, 4, 3, 1]]
    dp = [0] * 5
    hst = set([0])
    for i in range(len(arr)-1):
        temp = set()
        temp_dp = [INF] * 5
        for foot in hst:
            if arr[i-1] != arr[i]:
                temp_dp[arr[i-1]] = min(temp_dp[arr[i-1]], cost[foot][arr[i]] + dp[foot])
                temp.add(arr[i-1])
            if foot != arr[i]:
                temp_dp[foot] = min(temp_dp[foot], cost[arr[i-1]][arr[i]] + dp[foot])
                temp.add(foot)
        hst = temp
        dp = temp_dp
    print(min(dp))
    return
solution()
