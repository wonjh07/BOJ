import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for x in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 첫째줄 값을 초기화
for x in range(1, N):
    if lst[0][x] == 1:  # 단, 1을 만나면 더 나아갈 수 없으므로 break
        break
    dp[0][x] = [1, 0, 0]

# 두번째 줄부터 dp
for i in range(1, N):
    for j in range(2, N):  # j 가 줄어드는 방향은 존재하지 않으므로 최소인덱스가 2
        if lst[i][j] == 0: # 현재 인덱스가 벽이 아닐때
            # 수평으로 올수 있는 경로의 인덱스의 대각선,수평 이동 수를 더함
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            # 수직으로 올수 있는 경로의 인덱스의 대각선,수직 이동 수를 더함
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
            # 대각선으로 올수 있는 경로의 조건, 직선과 수직모두 벽이 없을 때
            if lst[i-1][j] == 0 and lst[i][j-1] == 0:
                #대각선경로의 인덱스의 모든 가짓수를 더함
                dp[i][j][1] = sum(dp[i-1][j-1])

print(sum(dp[N-1][N-1]))
