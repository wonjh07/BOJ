import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    rv = 1
    p = input().rstrip()
    n = int(input().rstrip())
    arr = list(input().rstrip().rstrip(']').lstrip('[').split(','))
    q = deque(arr)
    err = 0
    for i in p:
        if i == 'D' and not n:
            err = 1
            break
        if i == 'R':
            rv *= -1
        else:
            n -= 1
            if rv == 1:
                q.popleft()
            else:
                q.pop()
    if err:
        print('error')
    else:
        if rv == -1:
            q = list(q)[::-1]
        print('[' + ','.join(q) + ']')