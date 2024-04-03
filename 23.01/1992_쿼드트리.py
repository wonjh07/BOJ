import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    arr = [ list(input().rstrip()) for _ in range(N) ]
    if N == 1:
        print(arr[0][0])
        return

    def solve(s, n):
        temp = ''
        if n == 1:
            for i in range(2):
                for j in range(2):
                    temp = temp + arr[s[0] + i][s[1] + j]
        elif n > 1:
            for i in range(2):
                for j in range(2):
                    y, x = (s[0] + i * n, s[1] + j * n)
                    temp = temp + solve((y, x), n // 2)

        if temp == '0000':
            return '0'
        elif temp == '1111':
            return '1'
        else:
            return '(' + temp + ')'

    ans = solve((0,0), N // 2)
    print(ans)
    return
main()