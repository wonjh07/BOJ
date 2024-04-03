def check(x, y):
    global max_v
    stk = []
    ## 길쭉이
    if y < M-3:
        stk.append(sum(arr[x][y:y+4]))
    if x < N-3:
        tmp = 0
        for k in range(4):
            tmp += arr[x+k][y]
        stk.append(tmp)
    ## 정사각형
    if x < N-1 and y < M-1:
        stk.append(sum(arr[x][y:y+2]) + sum(arr[x+1][y:y+2]))
    ## 지그재그
    if x < N-2 and y < M-1:
        stk.append(arr[x][y] + sum(arr[x+1][y:y+2]) + arr[x+2][y+1])
        stk.append(arr[x][y+1] + sum(arr[x+1][y:y+2]) + arr[x+2][y])
    if x < N-1 and y < M-2:
        stk.append(sum(arr[x][y:y+2]) + sum(arr[x+1][y+1:y+3]))
        stk.append(sum(arr[x][y+1:y+3]) + sum(arr[x+1][y:y+2]))
    ## 법규 + 기억자
    if x < N-1 and y < M-2:
        a = sum(arr[x][y:y+3])
        stk.append(a + arr[x+1][y])
        stk.append(a + arr[x+1][y+1])
        stk.append(a + arr[x+1][y+2])
    if x < N-2 and y < M-1:
        tmp = 0
        for k in range(3):
            tmp += arr[x+k][y]
        b = tmp
        stk.append(b + arr[x][y+1])
        stk.append(b + arr[x+1][y+1])
        stk.append(b + arr[x+2][y+1])
    if x > 0 and y < M-2:
        a = sum(arr[x][y:y+3])
        stk.append(a + arr[x-1][y])
        stk.append(a + arr[x-1][y+1])
        stk.append(a + arr[x-1][y+2])
    if x < N-2 and y > 0:
        tmp = 0
        for k in range(3):
            tmp += arr[x+k][y]
        b = tmp
        stk.append(b + arr[x][y-1])
        stk.append(b + arr[x+1][y-1])
        stk.append(b + arr[x+2][y-1])
    if stk:
        res = max(stk)
        if max_v < res:
            max_v = res


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
for i in range(N):
    for j in range(M):
        check(i, j)
print(max_v)