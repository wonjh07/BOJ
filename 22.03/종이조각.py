import sys
input = sys.stdin.readline


def papercut(ln, ssum, vst):
    global N, M, sol
    # 종이조각으로 가득차면 종료
    if ln == (N * M):
        if sol < ssum:
            sol = ssum
        return
    # 각 칸마다 종이조각 dfs
    for i in range(N):
        for j in range(M):
            if not vst[i][j]:
                # 좌우로 긴 종이조각
                tmp = ''
                tmp2 = [vst[u][:] for u in range(N)]
                for k in range(M-j):
                    if not vst[i][j+k]:
                        tmp2[i][j+k] = 1
                        tmp += lst[i][j+k]
                        papercut(ln+1+k, ssum+int(tmp), tmp2)
                # 위, 아래로 긴 종이조각
                # 한칸 짜리는 중복되지않게 건너뜀
                tmp = lst[i][j]
                tmp2 = [vst[u][:] for u in range(N)]
                tmp2[i][j] = 1
                for k in range(1, N-i):
                    if not vst[i+k][j]:
                        tmp2[i+k][j] = 1
                        tmp += lst[i+k][j]
                        papercut(ln+1+k, ssum+int(tmp), tmp2)
                return


N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
arr = [[0] * M for _ in range(N)]
sol = 0
papercut(0, 0, arr)
print(sol)
