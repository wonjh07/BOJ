from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
else:
    que = deque([[N, 0]])
    vst = [0] * 100001
    vst[N] = 1
    sol = 0
    while que:
        x, cnt = que.popleft()
        for i in [x+1, x-1, x*2]:
            if i == K:
                sol = cnt + 1
                break
            if 0 <= i <= 100000 and not vst[i]:
                vst[i] = 1
                que.append([i, cnt+1])
        if sol:
            break
    print(sol)