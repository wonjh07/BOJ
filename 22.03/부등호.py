import sys
input = sys.stdin.readline


def check_min(ln):
    global mn, stk, N
    if ln == N+1:
        mn = map(str, stk)
        return

    for i in range(10):
        if not vst[i]:
            if (lst[ln-1] == '>' and stk[-1] > i) or (lst[ln-1] == '<' and stk[-1] < i):
                vst[i] = 1
                stk.append(i)
                check_min(ln+1)
                if mn:
                    return
                vst[i] = 0
                stk.pop()


def check_max(ln):
    global mx, stk, N
    if ln == N+1:
        mx = map(str, stk)
        return

    for i in range(9, -1, -1):
        if not vst[i]:
            if (lst[ln-1] == '>' and stk[-1] > i) or (lst[ln-1] == '<' and stk[-1] < i):
                vst[i] = 1
                stk.append(i)
                check_max(ln+1)
                if mx:
                    return
                vst[i] = 0
                stk.pop()


N = int(input())
lst = list(input().rstrip().split())
vst = [0] * 10
stk = []
mn = ''
mx = ''

for a in range(10):
    vst[a] = 1
    stk = [a]
    check_min(1)
    vst[a] = 0
    if mn:
        break

stk = []
vst = [0] * 10
for b in range(9, -1, -1):
    vst[b] = 1
    stk = [b]
    check_max(1)
    vst[b] = 0
    if mx:
        break
print(''.join(mx))
print(''.join(mn))