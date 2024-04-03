import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))
result = {i: str(value) for value, i in enumerate(sort_arr)}
print(*[result[j] for j in arr])