case = int(input())
for i in range(case):
    a, b = list(map(int, input().split()))
    length = b - a
    j = 0
    while True:
        if length <= j * (j + 1):
            break
        j += 1

    if length <= j ** 2:
        print(j * 2 - 1)
    else:
        print(j * 2)
