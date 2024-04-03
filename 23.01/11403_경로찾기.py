import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())

arr = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
vst = [0] * N
ans = []

def solve(s):
    for j in range(N):
        if arr[s][j] and vst[j] == 0:
            vst[j] = 1
            solve(j)

for i in range(N):
    vst = [0] * N
    solve(i)
    ans.append(vst)
    
for a in ans:
    print(*a, sep=' ')