import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    R, C, T = map(int, input().rstrip().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(R)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    ap = []
    total = [0]

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                total[0] += arr[i][j]
            elif arr[i][j] == -1:
                ap.append(i)

    def dust_move():
        temp = [copy_arr[:] for copy_arr in arr]
        for r in range(R):
            for c in range(C):
                if temp[r][c] >= 5:
                    diff = temp[r][c] // 5
                    cnt = 0
                    for i in range(4):
                        a, b = r + dy[i], c + dx[i]
                        if 0 <= a < R and 0 <= b < C and arr[a][b] >= 0:
                            cnt += 1
                            arr[a][b] += diff
                    arr[r][c] -= (diff * cnt)
        return
    
    def air_purifier():
        for ap_i in range(2):
            k = ap[ap_i]
            negative = -1 if ap_i else 1
            di = 0
            arr[k][0] = -1
            wi, wj = k + dy[di] * negative, 0 + dx[di]
            if arr[wi][wj]:
                total[0] -= arr[wi][wj]
                arr[wi][wj] = 0
            while 1:
                if di == 0 and (wi == 0 or wi == R-1):
                    di = 1
                elif di == 1 and wj == C-1:
                    di = 2
                elif di == 2 and wi == k:
                    di = 3
                
                n_wi, n_wj = wi + dy[di] * negative, wj + dx[di]
                if n_wi == k and n_wj == 0:
                    break

                if arr[n_wi][n_wj]:
                    arr[wi][wj] = arr[n_wi][n_wj]
                    arr[n_wi][n_wj] = 0
                wi, wj = n_wi, n_wj
        return

    for _ in range(T):
        dust_move()
        air_purifier()

    print(total[0])
    return

main()
 