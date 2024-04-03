import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input().rstrip())
ARR = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
ans = [0, 0]

def solve(arr, sp, ep):
    num = ((ep[0] - sp[0]) + (ep[1] - sp[1])) / 2 + 1
    temp = [0, 0]
    if num > 2:
        a = solve(arr, sp, (ep[0] - int(int(num/2)), ep[1] - int(int(num/2))))
        b = solve(arr, (sp[0], sp[1] + int(num/2)), (ep[0] - int(num/2), ep[1]))
        c = solve(arr, (sp[0] + int(num/2), sp[1]), (ep[0], ep[1] - int(num/2)))
        d = solve(arr, (sp[0] + int(num/2), sp[1] + int(num/2)), ep)
        temp[0] = a[0] + b[0] + c[0] + d[0]
        temp[1] = a[1] + b[1] + c[1] + d[1]
    
    elif num == 2:
        for i in range(sp[0], ep[0]+1):
            for j in range(sp[1], ep[1]+1):
                if arr[i][j] == 0:
                    temp[0] += 1
                else:
                    temp[1] += 1
    if (temp[0] == 4) & (temp[1] == 0):
        return [1, 0]
    elif (temp[0] == 0) & (temp[1] == 4):
        return [0, 1]
    else:
        return temp

ans = solve(ARR, (0, 0), (N-1, N-1))

print(*ans, sep='\n')