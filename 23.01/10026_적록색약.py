import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(N)]
vst1 = [[0] * N for _ in range(N)]
vst2 = [[0] * N for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ans1, ans2 = 0, 0

def solve1(a1, b1):
    c = arr[a1][b1]
    for d in range(4):
        y, x = a1 + dy[d], b1 + dx[d]

        if not (0 <= y < N and 0 <= x < N):
            continue

        if not vst1[y][x] and arr[y][x] == c:
            vst1[y][x] = 1
            solve1(y, x)
    return

def solve2(a2, b2):
    c = arr[a2][b2]
    if c == 'R' or c == 'G':
            c = 'R'

    for d in range(4):
        y, x = a2 + dy[d], b2 + dx[d]
        if not (0 <= y < N and 0 <= x < N):
            continue

        temp = arr[y][x]

        if temp == 'R' or temp == 'G':
            temp = 'R'

        if not vst2[y][x] and temp == c:
            vst2[y][x] = 1
            solve2(y, x)
    return

for i in range(N):
    for j in range(N):
        if not vst1[i][j]:
            vst1[i][j] = 1
            solve1(i, j)
            ans1 += 1
        
        if not vst2[i][j]:
            vst2[i][j] = 1
            solve2(i, j)
            ans2 += 1

print(ans1)
print(ans2)