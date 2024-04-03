from sys import stdin as s
s = open("input.txt", "rt")
check = [0] * 42

N = [int(s.readline().rstrip()) for _ in range(10)]

for i in range(0, len(N)):
    check[N[i] % 42] += 1

cnt = 0

for j in check:
    if j != 0:
        cnt += 1

print(cnt)
