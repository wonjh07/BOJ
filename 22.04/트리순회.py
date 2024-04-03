import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def pre_order(n):
    if n != '.':
        sol1.append(n)
        pre_order(v[ord(n) - 65][0])
        pre_order(v[ord(n) - 65][1])


def in_order(n):
    if n != '.':
        in_order(v[ord(n) - 65][0])
        sol2.append(n)
        in_order(v[ord(n) - 65][1])


def post_order(n):
    if n != '.':
        post_order(v[ord(n) - 65][0])
        post_order(v[ord(n) - 65][1])
        sol3.append(n)


N = int(input())
v = [[] for _ in range(N)]
sol1 = []
sol2 = []
sol3 = []
for _ in range(N):
    st, a, b = input().split()
    v[ord(st)-65] = [a, b]

pre_order('A')
print(''.join(sol1))
in_order('A')
print(''.join(sol2))
post_order('A')
print(''.join(sol3))
