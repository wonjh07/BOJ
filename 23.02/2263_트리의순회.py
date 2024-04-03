import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve(i, p, n):
    root = P[p[1]]
    if not ANS[0]:
        print(root, end='')
        ANS[0] = 1
    else:
        print('', root, end='')
    if n > 1:
        i_root = node[root]
        temp = i_root - i[0]
        if i_root > i[0]:
            solve((i[0], i_root-1), (p[0], p[0] + temp -1), temp)
        if i_root+1 <= i[1]:
            solve((i_root+1, i[1]), (p[0]+temp, p[1]-1), n - 1 - temp)
    return

N = int(input().rstrip())
I = list(map(int, input().rstrip().split()))
P = list(map(int, input().rstrip().split()))
node = [0] * (N+1)
for i in range(N):
    node[I[i]] = i
ANS = [0]
solve((0, N-1), (0, N-1), N)