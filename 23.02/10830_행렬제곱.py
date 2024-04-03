import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def mat_multi(x, y, mem, N, n):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += mem[x][i][k] * mem[y][k][j] % 1000
                temp = temp % 1000
            res[i][j] = temp
    mem[n] = res
    return

def solve(A, n, mem, N):
    if n in mem:
        return
    sp = n//2
    if sp not in mem:
        solve(A, sp, mem, N)
    if sp*2 not in mem:
        mat_multi(sp, sp, mem, N, sp*2)
    if n % 2:
        mat_multi(n-1, 1, mem, N, n)
    return

def main():
    N, B = map(int, input().rstrip().split())
    A = [list(map(int, input().rstrip().split())) for _ in range(N)]
    mem = {1: A}
    if B == 1:
        for i in range(N):
            for j in range(N):
                mem[1][i][j] %= 1000
    else:
        solve(A, B, mem, N)
    for m in mem[B]:
        print(*m, sep=' ')
    return
main()
