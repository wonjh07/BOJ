import sys
input = sys.stdin.readline

K = int(input())
x = y = 0
stk = [0] * 6
idx = [0] * 6

for i in range(6):
    idx[i], stk[i] = map(int, input().split())

j = 5
while j >= 0:
    if idx[j] == idx[j-2] and idx[j-1] == idx[j-3]:
        print((stk[j-4] * stk[j-5] - stk[j-1] * stk[j-2]) * K)
        break
    j -= 1

'''
4 2 3 1 3 1  
2 3 1 3 1 4
3 1 3 1 4 2
1 3 1 4 2 3
3 1 4 2 3 1
1 4 2 3 1 3
'''