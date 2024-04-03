import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
vst = [0] * 26
W = []
cnt = []
lv = [[] for _ in range(11)]
cvt = {}
sol = 0
for _ in range(N):
    w = input().rstrip()
    W.append(w)
    ln = len(w)
    for i in range(ln):
        vst[ord(w[i])-65] += 10 ** (ln-i)

for i in range(26):
    if vst[i]:
        cnt.append([vst[i], i])

tmp = 9
for a, b in sorted(cnt, reverse=True):
    cvt[chr(b+65)] = str(tmp)
    tmp -= 1


for i in W:
    tmp = ''
    for si in i:
        tmp += cvt[si]
    sol += int(tmp)

print(sol)
