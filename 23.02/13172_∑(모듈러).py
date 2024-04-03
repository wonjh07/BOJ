import sys, math
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 1000000007
MOD2 = 1000000005

def solve(n, sq):
    half = sq // 2
    if sq == 1:
        return n
    if sq % 2:
        res = ((solve(n, half) ** 2 % MOD) * n) % MOD
    else:
        res = (solve(n, half) ** 2) % MOD
    return res

def main():
    M = int(input().rstrip())
    ans = 0
    for _ in range(M):
        b, a = map(int, input().split())
        gcd = math.gcd(b, a)
        b, a = b // gcd, a // gcd
        m_inverse = solve(b, MOD2)
        ans += ((m_inverse * a) % MOD)
        ans %= MOD
    print(ans)
    return
main()
