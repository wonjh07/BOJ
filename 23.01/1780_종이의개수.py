import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
time = 0

def solve(s, n):
    cnt = [0, 0, 0]
    if n == 1:
        cnt[arr[0][0]] += 1
        return cnt

    elif n == 3:
        for ii in range(3):
            for jj in range(3):
                time += 1
                cnt[arr[s[0] + ii][s[1] + jj]] += 1
            
    elif n > 3:
        idx = n // 3
        for i in range(3):
            for j in range(3):
                time += 1
                x = ((s[0] + i * idx), (s[1] + j * idx))
                a, b, c = solve(x, idx)
                cnt = [cnt[0] + a, cnt[1] + b, cnt[2] + c]

    if cnt == [0, 0, 9] or cnt == [0, 9, 0] or cnt == [9, 0, 0]:
        cnt = [cnt[0]//9, cnt[1]//9, cnt[2]//9]

    return cnt

ans = solve((0,0), N)
print(ans[-1])
print(ans[0])
print(ans[1])
