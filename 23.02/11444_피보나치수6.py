import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve(n):
    if n in mem:
        return mem[n]
    else:
        if n % 2:
            temp = (solve(n//2) ** 2) % mod + (solve(n//2 + 1) ** 2) % mod
        else:
            temp = (solve(n//2)) * (2 * solve(n//2 - 1) % mod + solve(n//2)) % mod
        mem[n] = temp % mod
    return temp % mod

n = int(input().rstrip())
mod = 1000000007
mem = {0 : 0, 1 : 1, 2: 1, 3: 2, 4: 3, 5: 5}
print(solve(n))
