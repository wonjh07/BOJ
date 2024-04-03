import sys, time
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def solve():
    start = time.time()
    N = int(input().rstrip())
    M = int(input().rstrip())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().rstrip().split())
        if arr[a][b] == 0 or arr[a][b] > c:
            arr[a][b] = c

    for n in range(1, N+1):
        for i in range(1, N+1):
            if i == n:
                continue
            for j in range(1, N+1):
                if j == n or j == i:
                    continue
                if arr[i][n] and arr[n][j]:
                    if arr[i][j]:
                        arr[i][j] = min(arr[i][j], arr[i][n] + arr[n][j])
                    else:
                        arr[i][j] = arr[i][n] + arr[n][j]
    for k in arr[1:]:
        print(*k[1:], sep=' ')
    print(time.time() - start)
    return
solve()