import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    N, K = map(int, input().rstrip().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0] * (K+1)
    for w, v in arr:
        for i in range(K, -1, -1):
            if w <= i:
                temp = dp[i-w] + v
                if temp > dp[i]:
                    dp[i] = temp
            else:
                break
    print(dp[K])
    return

solve()
# 함수로 만들어서 지역변수를 사용하면 훨씬 빨라진다.
