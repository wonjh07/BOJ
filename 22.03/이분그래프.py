import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(st):
    global sol
    for j in stk[st]:
        if vst[j] == 0:
            vst[j] = vst[st] * -1
            dfs(j)
        elif vst[j] == vst[st]:
            sol = 'NO'
            return 
        if sol == 'NO':
            return

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    vst = [0] * (V+1)
    stk = [[] for _ in range(V+1)]
    sol = 'YES'
    for _ in range(E):
        a, b = map(int, input().split())
        stk[a].append(b)
        stk[b].append(a)
    
    for i in range(1, V+1):
        if vst[i] == 0:
            vst[i] = 1
        dfs(i)
        if sol == 'NO':
            break
    print(sol)
