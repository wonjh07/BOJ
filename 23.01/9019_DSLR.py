import sys, time
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

T = int(input().rstrip())
C = ['D', 'S', 'L', 'R', 'D']
start = time.time()

for _ in range(T):
    ans = ''
    dp = [-1] * 10000
    dp2 = [-1] * 10000
    A, B = map(int, input().rstrip().split(' '))
    dp[A] = ''
    dp2[B] = ''
    q = deque([(A, 1), (B, 2)])
    while q:
        #출발점 뻗어 나가기
        a, t = q.popleft()
        if t == 1:
            for i in range(4):
                if C[i] == 'D':
                    tf = (a * 2) % 10000
                elif C[i] == 'S':
                    tf = 9999 if a == 0 else a - 1
                elif C[i] == 'L':
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[1:] + temp[0])
                elif C[i] == 'R':
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[-1] + temp[:-1])

                if dp2[tf] != -1:
                    ans = dp[a] + C[i] + dp2[tf]
                    break

                if dp[tf] == -1 or len(dp[tf]) > (len(dp[a]) + 1):
                    dp[tf] = dp[a] + C[i]
                    q.append((tf, 1))

        # 도착점 반대로 뻗어나가기
        if t == 2:
            for i in range(5):
                if i == 0:
                    if a % 2:
                        continue
                    tf = (a // 2)
                elif i == 1:
                    tf = 0 if a == 9999 else a + 1
                elif i == 2:
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[-1] + temp[:-1])
                elif i == 3:
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[1:] + temp[0])
                elif i == 4:
                    if a % 2:
                        continue
                    tf = ((a + 10000) // 2)

                if dp[tf] != -1:
                    ans = dp[tf] + C[i] + dp2[a]
                    break

                if dp2[tf] == -1 or len(dp2[tf]) > (len(dp2[a]) + 1):
                    dp2[tf] = C[i] + dp2[a]
                    q.append((tf, 2))

        if ans:
            break

    print(ans)
    print(time.time()-start)