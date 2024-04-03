from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    print(N)
else:
    que = deque([[N, 0]])
    vst = [-1] * 100001
    vst[N] = N
    sol = 0
    while que:
        x, cnt = que.popleft()
        for i in [x+1, x-1, x*2]:
            if i == K:
                sol = cnt + 1
                vst[i] = x
                break
            if 0 <= i <= 100000 and vst[i] == -1:
                vst[i] = x
                que.append([i, cnt+1])
        if sol:
            break
    print(sol)
    j = K
    stk = [j]
    while j != N:
        stk.append(vst[j])
        j = vst[j]
    print(*stk[::-1])
