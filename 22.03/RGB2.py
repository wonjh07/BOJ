import sys
input = sys.stdin.readline

N = int(input())
dpr = [[0, 0, 0] for _ in range(1001)]
dpb = [[0, 0, 0] for _ in range(1001)]
dpg = [[0, 0, 0] for _ in range(1001)]

R, G, B = map(int, input().split())
dpr[0] = [R, 2001, 2001]
dpg[0] = [2001, G, 2001]
dpb[0] = [2001, 2001, B]

for k in range(1, N):
    R, G, B = map(int, input().split())
    dpr[k][0] = min(dpr[k-1][1],dpr[k-1][2]) + R
    dpr[k][1] = min(dpr[k-1][0],dpr[k-1][2]) + G
    dpr[k][2] = min(dpr[k-1][0],dpr[k-1][1]) + B

    dpg[k][0] = min(dpg[k-1][1],dpg[k-1][2]) + R
    dpg[k][1] = min(dpg[k-1][0],dpg[k-1][2]) + G
    dpg[k][2] = min(dpg[k-1][0],dpg[k-1][1]) + B

    dpb[k][0] = min(dpb[k-1][1],dpb[k-1][2]) + R
    dpb[k][1] = min(dpb[k-1][0],dpb[k-1][2]) + G
    dpb[k][2] = min(dpb[k-1][0],dpb[k-1][1]) + B

print(min(dpr[N-1][1], dpr[N-1][2], dpg[N-1][0], dpg[N-1][2], dpb[N-1][0], dpb[N-1][1]))
