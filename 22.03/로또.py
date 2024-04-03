def dfs(st, ln):
    global vst, stk
    if ln == 6:
        print(*stk)
        return

    for i in range(st, N):
        if not vst[i] and stk[-1] < lst[i]:
            vst[i] = 1
            stk.append(lst[i])
            dfs(st+1, ln+1)
            vst[i] = 0
            stk.pop()
    return
    

while 1:
    N, *lst = map(int, input().split())
    if N == 0:
        break
    vst = [0] * N
    for k in range(0, N-5):
        vst[k] = 1
        stk = [lst[k]]
        dfs(1, 1)
    print()
