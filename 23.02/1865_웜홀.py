import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    TC = int(input().rstrip())
    for _ in range(TC):
        N, M, W = map(int, input().rstrip().split())
        arr = [['x'] * N for _ in range(N)]
        hst = [[] for _ in range(N)]
        vst = [0] * N
        cycle = 0

        for _ in range(M):
            S, E, T = map(int, input().rstrip().split())
            S, E = S-1, E-1
            if arr[S][E] == 'x' or arr[S][E] > T:
                arr[S][E] = T
                arr[E][S] = T
                hst[S].append(E)
                hst[E].append(S)

        for _ in range(W):
            S, E, T = map(int, input().rstrip().split())
            S, E = S-1, E-1
            if arr[S][E] == 'x' or arr[S][E] > -T:
                arr[S][E] = -T
                hst[S].append(E)

        for n in range(N):
            for i in range(N):
                for j in hst[i]:
                    if vst[j] > vst[i] + arr[i][j]:
                        vst[j] = vst[i] + arr[i][j]
                        if n == N-1 and vst[j] < 0:
                            cycle = 1
                            break
        if cycle:
            print('YES')
        else:
            print('NO')

    return

solve()