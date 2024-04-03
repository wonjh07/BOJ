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
                vst.append(order(i, j))
        
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


for _ in range(N-1):
    a, b, c = map(int, input().split())
    vl[a].append((b, c))
    
order(1, 0)
print(sol)