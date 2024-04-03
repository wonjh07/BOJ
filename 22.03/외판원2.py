import sys
input = sys.stdin.readline

def dfs(ln, ssum, prv):
    global mn, vst
    if ln == N and mn > ssum:
        mn = ssum
        return
    if ln and not prv:
        return
    for i in range(N):
        if not vst[i] and W[prv][i]:
            vst[i] = 1
            dfs(ln+1, ssum+W[prv][i], i)
            vst[i] = 0


N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))

mn = 100000000
vst = [0] * N
dfs(0, 0, 0)

print(mn)
