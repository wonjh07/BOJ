import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
s = input().rstrip()
cp = 'I' + ('OI' * N)
stk = []
tmp = 0
cnt = 0
i = 0
while i < M:
    if s[i] == 'I':
        i += 1
        while 1:
            if s[i:i+2] == 'OI':
                tmp += 1
                i += 2
            else:
                tmp = 0
                break
            if tmp == N:
                cnt += 1
                while 1:
                    if s[i:i+2] == 'OI':
                        cnt += 1
                        i += 2
                    else:
                        tmp = 0
                        break
    else:
        i += 1

print(cnt)

