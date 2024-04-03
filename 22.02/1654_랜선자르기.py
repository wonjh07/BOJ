import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
E = max(lst)

start = 1
end = E
max_v = 0
while start <= end:
    middle = (start + end) // 2

    tmp = 0
    for i in lst:
        tmp += (i // middle)
    if tmp >= K and middle > max_v:
        max_v = middle

    if tmp < K:
        end = middle - 1

    elif tmp >= K:
        start = middle + 1

print(max_v)