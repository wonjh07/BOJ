import sys
input = sys.stdin.readline

N = int(input())

history = [0] * 100001
dp = []
dp2 = dp

i = 1
while i * i <= N:
    if i * i == N:
        sol = 1
    dp.append(i * i)
    history[i*i] += 1
    i += 1

idx = 1
while not history[N]:
    idx += 1
    tmp = []
    for i in dp2:
        for j in dp:
            if i + j > N:
                break
            if not history[i+j]:
                tmp.append(i+j)
                history[i+j] += 1
        dp2 = tmp
        if history[N]:
            break
print(idx)