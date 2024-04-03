case = int(input())
for i in range(case):
    h, w, n = list(map(int, input().split()))
    if n % h == 0:
        floor = h
        number = n // h
    else:
        floor = n % h
        number = n // h + 1
    print(f'{floor * 100 + number}')
