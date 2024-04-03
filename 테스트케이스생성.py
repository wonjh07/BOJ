import random

def table(N, M, st, end):
    lst = []
    C = list(range(st, end+1))
    for _ in range(N):
        tmp = []
        for _ in range(M):
            tmp.append(random.choice(C))
        lst.append(tmp)
    print(N, M)
    for k in range(N):
        print(*lst[k], sep='')

# 테이블 생성 0 or 1)
# arr 사이즈
N, M = 4, 4

# 생성 숫자 범위
st, end = 0, 9

table(N, M, st, end)