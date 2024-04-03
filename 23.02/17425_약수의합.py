import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    T = int(input().rstrip())
    mod = 2
    lst = [0] * T
    mx = 0

    for t in range(T):
        lst[t] = int(input().rstrip())
        if mx < lst[t]:
            mx = lst[t]
        
    arr = [i + 1 for i in range(mx + 1)]
    arr[0], arr[1] = 0, 1

    while mod <= mx//2:
        for j in range(mod * 2, mx + 1, mod):
            arr[j] += mod
        mod += 1

    for k in range(1, mx + 1):
        arr[k] = arr[k-1] + arr[k]

    for a in lst:
        print(arr[a])
    
    return
solve()