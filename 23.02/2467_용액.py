import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    spl = list(map(int, input().rstrip().split()))
    mn = 10e10
    ans = [0, 0]
    a, b = 0, N-1
    while a != b:
        temp = abs(spl[a] + spl[b])
        if temp == 0:
            ans[0], ans[1] = spl[a], spl[b]
            break

        if mn > temp:
            mn = temp
            ans[0], ans[1] = spl[a], spl[b]

        if abs(spl[a]) >= abs(spl[b]):
            a += 1
        else:
            b -= 1

    print(*ans)
    return
main()
