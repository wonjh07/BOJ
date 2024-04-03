a, b = map(int, input().split())

prime = [0 for x in range(b + 1)]
prime[1] = 1

for i in range(2, b + 1):
    if i * i > b:
        break
    if prime[i] == 0:
        for j in range(i * i, b + 1, i):
            prime[j] = 1

for k in range(a, b + 1):
    if prime[k] == 0:
        print(k)
