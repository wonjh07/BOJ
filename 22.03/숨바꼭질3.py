from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
else:
    que = deque([[N, 0]])
    vst = [-1] * 100001
    vst[N] = 0
    sol = 100001
    while que:
        x, cnt = que.popleft()
        if sol >= cnt:
            for i, j in [[x*2, 0], [x+1, 1], [x-1, 1]]:
                tmp = cnt + j
                if i == K:
                    if sol > tmp:
                        sol = tmp
                elif 0 <= i <= 100000:
                    if vst[i] == -1 or (tmp < vst[i] and tmp<=sol):
                        vst[i] = tmp
                        que.append([i, tmp])
    print(sol)
