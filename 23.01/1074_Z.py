import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, y, x = map(int, input().rstrip().split())
cnt = 0
ans = 0
sp = (0, 0)
ep = (2 ** N - 1, 2 ** N - 1)

def solve(sp, ep, n):
    global cnt, ans
    if ans:
        return

    if n == 0:
        if sp == (y, x):
            ans = cnt
            return

    if n >= 1:
        spt = 2**(n-1)
        lst = [
            [(sp[0], sp[1]), (ep[0] - spt, ep[1] - spt)],
            [(sp[0], sp[1] + spt), (ep[0] - spt, ep[1])],
            [(sp[0] + spt, sp[1]), (ep[0], ep[1] - spt)],
            [(sp[0] + spt, sp[1] + spt), (ep[0], ep[1])],
        ]
        for i in lst:
            if (i[0][0] <= y <= i[1][0]) & (i[0][1] <= x <= i[1][1]):
                solve(i[0], i[1], n-1)
                break
            else:
                cnt += (2 ** (n-1)) * (2 ** (n-1))
    return

solve(sp, ep, N)
print(ans)