import sys
input = sys.stdin.readline

def dfs(st, stk, ln):
    if ln == 5:
        return 1
    for i in lst[st]:
        if i not in stk:
            if dfs(i, stk+[i], ln+1):
                return 1
    return 0


N, M = map(int, input().split())
sol = 0
lst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(N):
    if dfs(i, [i], 1):
        sol = 1
        break

print(sol)
