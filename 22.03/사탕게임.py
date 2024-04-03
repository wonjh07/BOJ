import sys
input = sys.stdin.readline

def checkw(k):
    global sol
    mx = 0
    cnt = 0
    prv = arr[k][0]

    for ii in range(N):
        if prv == arr[k][ii]:
            cnt += 1
        else:
            cnt = 1
        prv = arr[k][ii]
        if mx < cnt:
            mx = cnt
    
    if sol < mx:
        sol = mx

def checkh(k):
    global sol
    mx = 0
    cnt = 0
    prv = arr[0][k]

    for ii in range(N):
        if prv == arr[ii][k]:
            cnt += 1
        else:
            cnt = 1
        prv = arr[ii][k]
        if mx < cnt:
            mx = cnt
    
    if sol < mx:
        sol = mx


N = int(input())
arr = [[] for _ in range(N)]
for x in range(N):
    arr[x] = list(input().rstrip())
sol = 0
for i in range(N):
    for j in range(N):
        if j < N-1:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            checkw(i)
            checkh(j)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if j > 0:
            arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
            checkh(j)
            arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        if i < N-1:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            checkw(i)
            checkh(j)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        if i > 0:
            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
            checkw(i)
            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
print(sol)
