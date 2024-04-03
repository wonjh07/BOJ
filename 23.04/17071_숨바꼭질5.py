import sys
sys.stdin = open("input.txt", "rt")

def main():
    from collections import deque

    INF = float('inf')
    N, K = map(int, input().split())
    vst = [[INF, INF] for _ in range(500001)]
    vst[N] = [0, 0]
    seq = {}
    now = K
    ans = INF
    len_idx = 0

    for i in range(500000):
        now += i
        if now > 500000:
            len_idx = i - 1
            break
        seq[now] = i

    def check(i, num):
        if not i in seq:
            return False
        if seq[i] >= num and not (seq[i] - num) % 2:
            return seq[i]
        else:
            return False
        
    res = check(N, 0)
    if res and ans > res:
        ans = res

    q = deque([(1, N)])
    if N == K:
        return 0
    while q:
        n, c = q.popleft()
        if n > ans or n > len_idx:
            break
        target = [c*2, c+1, c-1]
        for i in target:
            e = 1 if n % 2 else 0
            if 0 <= i <= 500000 and vst[i][e] > n:
                vst[i][e] = n
                res = check(i, n)
                if res and ans > res:
                    ans = res
                if not res:
                    q.append((n+1, i))
    if ans == INF:
        return -1
    return ans
print(main())