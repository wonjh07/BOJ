# 빠른 A + B
# sys.stdin 을 사용해 시간 단축

import sys

case = sys.stdin.readline()

for i in range(int(case)):
    nums = str(sys.stdin.readline()).rstrip()
    a, b = map(int, nums.split(' '))
    print(a + b)
