import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
stack = [0, card[0]]

for i in range(2, N+1):
    maxv = card[i-1]
    for j in range(1, i):
        if maxv < stack[j] + stack[i-j]:
            maxv = stack[j] + stack[i-j]
    stack.append(maxv)

print(stack[N])