import sys
input = sys.stdin.readline

l_stack = list(input().rstrip('\n'))
r_stack = []
N = int(input())
for _ in range(N):
    order = input().rstrip('\n').split()
    if order[0] == 'P':
        l_stack.append(order[1])
    if order[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    if order[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    if order[0] == 'B' and l_stack:
        l_stack.pop()

print(''.join(l_stack) + ''.join(r_stack[::-1]))
