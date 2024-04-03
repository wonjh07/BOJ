import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
E = max(lst)

start = 0
end = E
middle = (start + end) // 2
while start <= end:
    tmp = 0
    tmp = sum(i - middle if i > middle else 0 for i in lst)
    if tmp < M:
        end = middle - 1
        middle = (start + end) // 2
    else:
        start = middle + 1
        middle = (start + end) // 2
print(middle)
