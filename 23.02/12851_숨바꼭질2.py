import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
INF = float('inf')

# 140ms 단방향 탐색
def main():
    N, K = map(int, input().split())
    cnt, mn = 0, INF
    vst = [INF] * 1000001
    vst[N] = 0
    q = deque([(1, N)])
    if N == K:
        print(0)
        print(1)
        return
    while q:
        n, c = q.popleft()
        target = [c*2, c+1, c-1]
        if mn < n:
            continue
        for i in target:
            if 0 <= i <= 100000 and vst[i] >= n:
                vst[i] = n
                if i == K:
                    if mn == n:
                        cnt += 1

                    elif mn > n:
                        mn = n
                        cnt = 1
                    continue
                q.append((n+1, i))
    print(mn)
    print(cnt)
    return
main()

'''
# 양방향 탐색에서 서로 같은 길이 중복되는 문제가 생김

import sys, heapq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = float('inf')

def main():
    N, K = map(int, input().rstrip().split())
    cnt, mn = 0, INF
    f_vst = [INF] * 100001
    b_vst = [INF] * 100001
    f_vst[N], b_vst[K] = 0, 0
    q = []
    heapq.heappush(q, (1, N, 0))
    heapq.heappush(q, (1, K, 1))
    while q:
        n, c, d = heapq.heappop(q)
        if d == 0:
            target = [c*2, c+1, c-1]
            vst1, vst2 = f_vst, b_vst
        else:
            target = [c // 2 if not c % 2 else -1, c-1, c+1]
            vst1, vst2 = b_vst, f_vst

        for i in target:
            if 0 <= i <= 100000 and vst1[i] >= n:
                vst1[i] = n
                if vst2[i] != INF:
                    temp = vst2[i] + n
                    if mn == temp:
                        #print('최소', temp, i, d)
                        cnt += 1
                        continue

                    elif mn > temp:
                        #print('갱신', temp, i, d)
                        mn = temp
                        cnt = 1
                        continue

                if mn <= n:
                    continue

                heapq.heappush(q, (n+1, i, d))
    print(mn)
    print(cnt)
    return
main()
'''