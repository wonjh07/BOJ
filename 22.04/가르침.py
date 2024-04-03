import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def dfs(ln, x):
    global mx
    if ln == T:
        cnt = 0
        for wd in arr:
            for lt in wd:
                if not vst2[lt]:
                    break
            else:
                cnt += 1
        if mx < cnt:
            mx = cnt
        return

    if x < len(stk):
        if vst[stk[x]]:
            vst2[stk[x]] = 1
            dfs(ln+1, x+1)
            vst2[stk[x]] = 0
        dfs(ln, x+1)


N, K = map(int, input().split())
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    T = K-5
    mx = 0
    vst = [0] * 26
    stk = []
    arr = [set() for _ in range(N)]
    for i in range(N):
        word = input().rstrip()
        for j in set(word[4:len(word)-4]):
            if j not in ('a', 'c', 'n', 't', 'i'):
                vst[ord(j)-97] = 1
                arr[i].add(ord(j)-97)
    for i in range(26):
        if vst[i]:
            stk.append(i)
    vst2 = [0] * 26
    if len(stk) <= T:
        print(N)
    else:
        dfs(0, 0)
        print(mx)