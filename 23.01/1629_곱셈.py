import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())
temp = A % C

# 분할정복
def solve(b):
    if b == 1:
        return temp
    elif b % 2:
        return ((solve(b//2) ** 2) * temp) % C
    else:
        return (solve(b//2) ** 2) % C

print(solve(B))