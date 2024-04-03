import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M == 0:
    B = []
else:
    B = list(map(str, input().split()))
now = 100
ans0 = abs(now-N)
ans1 = 500000
ans2 = 500000
j = 0
while N-j >= 0:
    lbl = 0
    for i in str(N-j):
        if i in B:
            lbl = 1
            break
    if not lbl:
        ans1 = len(str(N-j)) + j
        break
    j+=1

j = 0
while 1:
    if len(str(N+j)) + j > ans1:
        break
    lbl = 0
    for i in str(N+j):
        if i in B:
            lbl = 1
            break
    if not lbl:
        ans2 = len(str(N+j)) + j
        break
    j+=1
print(min(ans0, ans1, ans2))