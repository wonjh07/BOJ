import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    x, y, M, N = map(int, input().split())
    if x < y:
        x, y, M, N = y, x, N, M
    st = N
    cnt = N
    a, b = x, y
    while b > 0:
        a, b = b, a % b
    end = (x * y) // a
    while 1:
        if cnt > end:
            cnt = -1
            break
        if st == M:
            break
        st += y
        cnt += y
        if st > x:
            st = (st-1) % x
            st += 1
    print(cnt)
