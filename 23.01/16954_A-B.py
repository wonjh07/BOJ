import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
q = deque([(A, 1)])
ans = -1
while q:
    n, c = q.popleft()
    a, b = 0, 0
    if n * 2 <= B:
        a = n * 2

    if n * 10 + 1 <= B:
        b = n * 10 + 1 

    if a == B or b == B:
        ans = c + 1
        break

    if 0 < a:
        q.append((a, c+1))

    if 0 < b:
        q.append((b, c+1))

    if ans != -1:
        break

print(ans)

'''
메모리 초과

A, B = map(int, input().rstrip().split())
vst = [[-1, -1] for _ in range(B+1)]
q = deque([(A, 1, 0), (B, 1, 1)])
vst[A][0], vst[B][1] = 0, 0
ans = -1
while q:
    n, c, t = q.popleft()
    if t == 0:
        a, b = 0, 0
        if n * 2 <= B:
            a = n * 2

        if n * 10 + 1 <= B:
            b = n * 10 + 1 

        if vst[a][1] != -1:
            ans = c + 1 + vst[a][1]
            break
        elif vst[b][1] != -1:
            ans = c + 1 + vst[b][1]
            break

        if 0 < a < B and (vst[a][0] == -1 or vst[a][0] > c):
            vst[a][0] = c
            q.append((a, c+1, 0))

        if 0 < b < B and (vst[b][0] == -1 or vst[b][0] > c):
            vst[b][0] = c
            q.append((b, c+1, 0))

    else:
        a, b = 0, 0
        if not n % 2:
            a = n // 2

        if n % 10 == 1:
            b = n // 10 

        if vst[a][0] != -1:
            ans = c + 1 + vst[a][0]
            break
        elif vst[b][0] != -1:
            ans = c + 1 + vst[b][0]
            break

        if a > A and (vst[a][1] == -1 or vst[a][1] > c):
            vst[a][1] = c
            q.append((a, c+1, 1))

        if b > A and (vst[b][1] == -1 or vst[b][1] > c):
            vst[b][1] = c
            q.append((b, c+1, 1))

    if ans != -1:
        break

print(ans)

'''