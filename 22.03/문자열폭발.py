import sys
input = sys.stdin.readline
from collections import deque

word = deque(list(input().rstrip()))
bomb = list(input().rstrip())
lnw = len(word)
lnb = len(bomb)
stk = []
tmp = []

while word:
    if word[0] == bomb[0]:
        tmp.append(word.popleft())
        j = [1]
        while j and word:
            if j[-1] == lnb:
                if tmp[len(tmp)-lnb:len(tmp)] == bomb:
                    for _ in range(lnb):
                        tmp.pop()
                    j.pop()
                else:
                    stk.extend(tmp)
                    tmp = []
                    j.pop()
                    break
            elif word[0] == bomb[0]:
                j.append(1)
                tmp.append(word.popleft())
            elif word[0] == bomb[j[-1]]:
                tmp.append(word.popleft())
                j[-1] += 1
            else:
                stk.extend(tmp)
                tmp = []
                j.pop()
                break
    else:
        stk.append(word.popleft())
if not word and tmp:
    if tmp != bomb:
        stk.extend(tmp)

if stk:
    print(''.join(stk))
else:
    print('FRULA')
