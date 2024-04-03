import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(1, N+1))

while 1:
    print(*lst)
    d = -1
    og = 0
    for i in range(N-1, 0, -1):
        if lst[i] > lst[i-1]:
            d = i-1
            og = lst[i-1]
            lst[i], lst[i-1] = lst[i-1], lst[i]
            break

    for j in range(d+2, N):
        if og < lst[j] and lst[d] > lst[j]:
            lst[d], lst[j] = lst[j], lst[d]

    if d == -1:
        break
    else:
        lst[d+1:] = sorted(lst[d+1:])