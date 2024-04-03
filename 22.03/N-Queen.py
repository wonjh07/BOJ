def dfs(y):
    global cnt
    if y == N:
        cnt += 1
        return 1

    for x in range(N):
        if not vst[x] and not vst2[y+x] and not vst3[x-y]:
            vst[x] = vst2[y+x] = vst3[x-y] = 1
            if dfs(y+1):
                vst[x] = vst2[y+x] = vst3[x-y] = 0
                break
            vst[x] = vst2[y+x] = vst3[x-y] = 0
    return 0

N = int(input())
cnt = 0
cot = 0
vst = [0] * N
vst2 = [0] * (N * 2 - 1)
vst3 = [0] * (N * 2 - 1)

for j in range(N//2):
    cot += 1
    vst[j] = vst2[j] = vst3[j] = 1
    dfs(1)
    vst[j] = vst2[j] = vst3[j] = 0
cnt *= 2
if N % 2:
    j = N // 2
    vst[j] = vst2[j] = vst3[j] = 1
    dfs(1)
print(cnt)
