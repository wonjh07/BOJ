import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def order(n, ssm):
    global sol
    if n <= N:
        vst = []
        tssm = 0
        
        if vl[n]:
            for i, j in vl[n]:
                if i != n and not vs[i]:
                    vs[i] = 1
                    vst.append(order(i, j))
                    vs[i] = 0
        
        if vst:
            tmp = sorted(vst)
            tssm = tmp[-1]
            if len(tmp) >= 2:
                tssm += tmp[-2]

            if sol < tssm:
                sol = tssm
            ssm += tmp[-1]

        return ssm

N = int(input())
sol = 0
vl = [[] for _ in range(N+1)]
vs = [0] * (N+1)

for _ in range(N):
    a, *b = map(int, input().split())
    for i in range(0, len(b)-1, 2):
        vl[a].append((b[i], b[i+1]))

vs[1] = 1
order(1, 0)
print(sol)