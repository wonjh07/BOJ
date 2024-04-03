import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
dp1 = [0] * N
dp2 = [0] * N
dp1[0] = num[0]
max_v = num[0]
for i in range(1, N):
    dp1[i] = max(dp1[i-1] + num[i], num[i])
    dp2[i] = max(dp1[i-1], dp2[i-1] + num[i])
    max_v = max(dp1[i], dp2[i], max_v)
print(max_v)