import sys
input = sys.stdin.readline

def dfs(st, ln, cnt_v, cnt_c):
    if ln == L and cnt_v >= 1 and cnt_c >= 2:
        print(''.join(stk))
        return
    for i in range(st, C):
        if not vst[i]:
            vst[i] = 1
            if lst[i] in vowel:
                cnt_v += 1
            else:
                cnt_c +=1
            stk.append(lst[i])
            dfs(i, ln+1, cnt_v, cnt_c)
            vst[i] = 0
            if stk.pop() in vowel:
                cnt_v -= 1
            else:
                cnt_c -= 1
    return


L, C = map(int, input().split())
lst = sorted(list(input().split()))
vst = [0] * C
stk = []
vowel = ['a', 'e', 'i', 'o', 'u']
dfs(0, 0, 0, 0)
