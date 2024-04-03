import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve(n, k, res):
    if k == 1:
        return
    if k >= 2:
        solve(n, k//2, res)
        spc = len(res[-1])
        for i in range(len(res)):
            temp = ''.join([res[i], ' ' * spc, res[i]])
            res.append(temp)
            spc -= 2
    return

def main():
    N = int(input().rstrip())
    k = N // 3
    ln = k * 6 // 2 - 1
    res = ['*', '* *', '*****']
    solve(N, k, res)
    for i in res:
        spc = ' ' * ln
        print(''.join([spc, i, spc]))
        ln -= 1
    return

main()
