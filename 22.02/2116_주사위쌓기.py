import sys
input = sys.stdin.readline

T = int(input())

max = 0
cvt = [5, 3, 4, 1, 2, 0]

num = [list(map(int, input().rstrip().split())) for _ in range(T)]
for i in range(6):
    up = num[0][i]
    result = 0
    for dice in num:
        down = up
        up = dice[cvt[dice.index(up)]]
        for j in range(6, 0 , -1):
            if j != up and j != down:
                result += j
                break
    if max < result:
        max = result
print(max)
