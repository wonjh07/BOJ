def check(num):
    label = 0
    cnt = 2
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                label += 1
                break
        if label:
            break

    for x in bingo[i]:
        if x != 0:
            cnt -= 1
            break

    for y in range(5):
        if bingo[y][j] != 0:
            cnt -= 1
            break

    if i == j:
        cnt += 1
        for xy in range(5):
            if bingo[xy][xy] != 0:
                cnt -= 1
                break
    if i + j == 4:
        cnt += 1
        for xy in range(5):
            if bingo[xy][4-xy] != 0:
                cnt -= 1
                break
    return cnt

bingo = [[] for _ in range(5)]
sol = 0
tot_cnt = 0
res = 0
for i in range(5):
    bingo[i] = list(map(int, input().split()))

for j in range(5):
    order = list(map(int, input().split()))
    for k in order:
        if not res:
            sol += 1
            tot_cnt += check(k)
            if tot_cnt >= 3:
                res = sol
                break
print(res)
