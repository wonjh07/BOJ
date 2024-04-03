import sys
input = sys.stdin.readline

N = int(input())

history = [0, 0, 1, 1]
if N <= 3:
    print(history[N])
else:
    for i in range(4, N + 1):
        tmp = []
        if not i % 3:
            tmp.append(history[i//3])
        if not i % 2:
            tmp.append(history[i//2])
        tmp.append(history[i-1])
        history.append(min(tmp) + 1)
    print(history[N])
