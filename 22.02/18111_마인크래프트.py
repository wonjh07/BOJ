import sys
input = sys.stdin.readline

lst = [0] * 257
N, M, B = map(int, input().split())
st = end = 0


for _ in range(N):
    for j in list(map(int, input().split())):
        lst[j] += 1

for i in range(257):
    if lst[i]:
        st = i
        break

for i in range(256, -1, -1):
    if lst[i]:
        end = i
        break

res = 1280000000
hst = 0
for i in range(st, end+1):
    cnt = B
    tmp = 0
    for j in range(st, end+1):
        if lst[j]:
            if j > i:
                cnt += (j - i) * lst[j]
                tmp += (j - i) * 2 * lst[j]
            else:
                cnt -= (i - j) * lst[j]
                tmp += (i - j) * lst[j]
    if cnt >= 0 and res >= tmp:
        res = tmp
        hst = i

print(res, hst)