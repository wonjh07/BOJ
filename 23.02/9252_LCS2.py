import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    a = input().rstrip()
    b = input().rstrip()
    dp = [''] * (len(b) + 1)

    def solve(i):
        temp = [''] * (len(b) + 1)
        for j in range(len(b)):
            if a[i] == b[j]:
                temp[j] = ''.join([dp[j-1], a[i]])
            else:
                if len(dp[j]) >= len(temp[j-1]):
                    temp[j] = dp[j]
                else:
                    temp[j] = temp[j-1]
        return temp
    
    for i in range(len(a)):
        dp = solve(i)

    print(len(dp[-2]))
    print(dp[-2])
    return

solve()
