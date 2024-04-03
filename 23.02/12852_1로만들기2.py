def main():
    N = int(input())
    dp = []
    vst = [0] * (N+1)

    for i in range(2, N + 1):
        a, b, c = i - 1, i // 3, i // 2
        vst[i] = vst[a] + 1
        dp[i][1] = dp[a][1]
        dp.append(i)

        if i % 3 == 0 and vst[b] + 1 < vst[i]:
            vst[i] = vst[b] + 1
            dp.append(i)

        if i % 2 == 0 and vst[c] + 1 < vst[c]:
            vst[i] = vst[c] + 1
            dp.append(i)

    print(dp[N][0])
    print(*(dp[N][1][::-1]))

    return
main()

'''
1등코드
# import sys
n = int(input())
d = {1: 0, 2: 1}
def s(n: int) -> int:
    if n in d:
        return d[n]
    t = 1 + min(s(n // 3) + n % 3, s(n // 2) + n % 2)
    d[n] = t
    return t
print(s(n))
while(n!=1):
  print(n, end = ' ')
  if n-1 in d and d[n] == d[n-1] + 1:
    n = n-1
  elif n//2 in d and d[n] == d[n//2] + 1 + n%2:

    if n%2 == 1:
      print(n-1, end = ' ')
    n = n//2

  else:

    if n%3 == 2:
      print(n-1, end = ' ')
      print(n-2, end = ' ')
    elif n%3 == 1:
      print(n-1, end = ' ')
    n = n//3
print(1)
'''

'''
# 양방향 BFS 탐색 실패
import heapq

def main():
    N = int(input().rstrip())
    INF = float('inf')
    vst = [[INF] * (N+1) for _ in range(2)]
    root = [[0] * (N+1) for _ in range(2)]
    vst[0][1], vst[1][N] = 0, 0
    q = [(1, 1, 0), (1, N, 1)]
    opp = [1, 0]
    ans = 0
    while q:
        v, i, t = heapq.heappop(q)
        if not t:
            chk = [i*3>N, i%2>N, i+1>N]
            way = [i*3, i*2, i+1]
        else:
            chk = [i%3, i%2, 0]
            way = [i//3, i//2, i-1]
        for j in range(3):
            e = way[j]
            if not chk[j] and e >= 1 and vst[t][j] > v:
                vst[t][e], root[t][e] = v, i
                if vst[opp[t]][e] != INF:
                    ans = e
                    break
                heapq.heappush(q, (v+1, e, t))
        if ans:
            break
    hst = []
    for t in range(1, -1, -1):
        temp = ans
        while 1:
            temp = root[t][temp]
            if temp == 0:
                break
            hst.append(temp)
            if temp == 1 or temp == N:
                break
        if t:
            hst.reverse()
            hst.append(ans)
    print(len(hst)-1)
    print(*hst, sep=' ')
    return
main()

'''