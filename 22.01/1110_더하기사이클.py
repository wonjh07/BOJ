# 더하기 사이클

n = int(input())
result = 0
count = 0
a, b = n // 10, n % 10

while True:
    result = (b * 10) + ((a + b) % 10)
    count += 1
    if result == n:
        print(count)
        break
    a, b = result // 10, result % 10
