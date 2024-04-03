import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
mx = sum(lst) + 2
cnt = [0] * (mx)

que = deque([(0, 0)])
while que:
    x, ssm = que.popleft()
    if x < N:
        cnt[lst[x]] = 1
        cnt[ssm+lst[x]] = 1
        que.append((x+1, ssm+lst[x]))
        cnt[ssm] = 1
        que.append((x+1, ssm))

for i in range(1, mx):
    if not cnt[i]:
        print(i)
        break 
