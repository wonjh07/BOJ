import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
arr = [[0] * (N+1) for _ in range(N+1)]
vst = [-1] * (N+1)
mn = float("inf")
p = 0

for _ in range(M):
    a, b = map(int, input().rstrip().split(' '))
    arr[a][b], arr[b][a] = 1, 1

def solve(i, n):
    for j in range(N+1):
        if arr[i][j] and ((vst[j] == -1) or (vst[j] > n)):
            vst[j] = n
            solve(j, n+1)
    return

for i in range(N+1):
    vst[i] = 0
    solve(i, 1)
    ans = 0
    for k in vst:
        if k > 0:
            ans += k
    if ans and mn > ans:
        mn = ans
        p = i
    vst = [-1] * (N+1)

print(p)