import sys
input = sys.stdin.readline

N = int(input())
LST = list(map(int, input().split()))
max_v = LST[0]

tmp = 0
for i in LST:
    if i >= 0:
        if tmp < 0:
            tmp = 0
        tmp += i
        if max_v < tmp:
            max_v = tmp
    else:
        if tmp < i < 0:
            tmp = 0
        tmp += i
        if max_v < tmp:
            max_v = tmp
        
print(max_v)