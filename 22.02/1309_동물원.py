import sys
input = sys.stdin.readline

N = int(input())
modi = 9901
dp1 = [0] * 100001
dp2 = [0] * 100001

dp1[1], dp2[1] = 0, 1

for i in range(2, N+1):
    dp1[i] = (dp1[i-1] + dp2[i-1] + dp2[i-1]) % modi
    dp2[i] = (dp1[i-1] + dp2[i-1]) % modi
sys.stdout.write(str((dp1[N] * 2 + dp2[N] * 3) % modi))