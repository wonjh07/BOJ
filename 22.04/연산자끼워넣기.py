import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, ssm):
    global mn, mx
    if x == N:
        if mx < ssm:
            mx = ssm
        if mn > ssm:
            mn = ssm
        return

    if sl[0]:
        sl[0] -= 1
        dfs(x+1, ssm + nl[x])
        sl[0] += 1
    if sl[1]:
        sl[1] -= 1
        dfs(x+1, ssm - nl[x])
        sl[1] += 1
    if sl[2]:
        sl[2] -= 1
        dfs(x+1, ssm * nl[x])
        sl[2] += 1
    if sl[3]:
        sl[3] -= 1
        if ssm < 0:
            tmp = -(-ssm // nl[x])
        else:
            tmp = ssm // nl[x]
        dfs(x+1, tmp)
        sl[3] += 1

N = int(input())
nl = list(map(int, input().split()))
sl = list(map(int, input().split()))
mx = float("-inf") 
mn = float("inf")

dfs(1, nl[0])
print(mx)
print(mn)