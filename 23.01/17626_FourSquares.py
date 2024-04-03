N = int(input().rstrip())
mn = 4
dp = [4] * (N + 1)

def solve(num, c):
    global mn
    temp = int(num ** 0.5)
    cnt = c + 1
    total = num - (temp ** 2)

    if (total == 0) and (cnt <= mn):
        mn = cnt
        return

    if cnt < mn:
        for i in range(temp, 0, -1):
            total = num - (i ** 2)
            if cnt < dp[total]:
                dp[total] = cnt
                solve(total, cnt)
            if mn == 1:
                return

    return

solve(N, 0)
print(mn)

'''
st = int(N ** 0.5)
for i in range(st, 0, -1):
    q = [i]
    total = N - (i ** 2)
    dp[total] = 1
    cnt = 1
    while total:
        time += 1
        j = int(total ** 0.5)
        q.append(j)
        total -= j ** 2
        cnt += 1
        if (cnt >= mn) or (cnt >= dp[total]):
            break
        dp[total] = cnt

    if (total == 0) and (cnt <= mn):
        mn = cnt
        print(q)

    if mn == 1:
        break
    
print(mn, time)

'''