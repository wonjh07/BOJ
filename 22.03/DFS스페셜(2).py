import sys
input = sys.stdin.readline

def dfs(st):
    root[st] = stk[:-1]
    if arr[st]:
        for i in arr[st]:
            if not vst[i]:
                vst[i] = 1
                stk.append(i)
                dfs(i)
                stk.pop()


def check():
    tmp = []
    for j in ans:
        if root[j] == tmp:
            tmp.append(j)
        else:
            while root[j] != tmp:
                if not tmp:
                    return 0
                tmp.pop()
            tmp.append(j)
    return 1


N = int(input())
arr = [[] for _ in range(N+1)]
vst = [0] * (N+1)
root = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = list(map(int, input().split()))

vst[1] = 1
stk = [1]
dfs(1)
print(check())