def track(lng):
    if lng == M:
        print(*stk)
        return
    else:
        cnt = [1] * 10001
        for j in range(0, N):
            if vst[j] and cnt[lst[j]]:
                vst[j] = 0
                cnt[lst[j]] = 0
                stk.append(lst[j])
                track(lng+1)
                vst[j] = 1
                stk.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
stk = []
vst = [1] * N
track(0)
