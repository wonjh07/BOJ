import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(st):
    global cnt
    for i in arr[st]:
        if not vst[i]:
            vst[i] = 1
            cnt += 1
            dfs(i)


N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
vst[1] = 1
dfs(1)

print(cnt)
