import sys
input = sys.stdin.readline


def f_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0


def beatme(ln):
    global sol, N
    if sol:
        return

    if stk:
        for u in range(ln):
            if f_sign(ssum[u]) != arr[u][ln-1]:
                return

    if ln == N:
        sol = stk[:]
        return

    for k in range(1, 11):
        stk.append(arr[ln][ln] * k)
        for u in range(ln+1):
            ssum[u] += arr[ln][ln] * k
        beatme(ln+1)
        stk.pop()
        if arr[ln][ln] == 0:
            break
        for u in range(ln+1):
            ssum[u] -= arr[ln][ln] * k
        


N = int(input())
lst = list(input().rstrip())
arr = [[0] * N for _ in range(N)]
stk = []
sol = []
ssum = [0] * N
a = 0
for i in range(N):
    for j in range(i, N):
        if lst[a] == '+':
            arr[i][j] = 1
        elif lst[a] == '-':
            arr[i][j] = -1
        a += 1
beatme(0)
print(*sol)
