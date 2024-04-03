import sys
input = sys.stdin.readline

prime = [0] * 1000001
prime[1] = 1

for i in range(2, 1000001):
    if i * i > 1000000:
        break
    if prime[i] == 0:
        for j in range(i * i, 1000001, i):
            prime[j] = 1


T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    result = ''
    if N == 0:
        break
    count = 0
    for i in range(3, N // 2 + 1, 2):
        if prime[i] == 0 and prime[N - i] == 0:
            count += 1
    if prime[2] == 0 and prime[N - 2] == 0:
        count += 1
    print(count)