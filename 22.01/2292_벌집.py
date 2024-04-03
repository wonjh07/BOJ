goal = int(input())
n = 1
result = (goal - 1)
while result > 0:
    result -= (6 * n)
    n += 1
print(n)