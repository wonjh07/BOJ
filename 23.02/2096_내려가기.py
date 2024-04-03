import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    dp_mx, dp_mn = arr[:], arr[:]
    for _ in range(N-1):
        arr = list(map(int, input().rstrip().split()))
        temp1, temp2 = [0, 0, 0], [0, 0, 0]
        temp1[0] = max(dp_mx[0], dp_mx[1]) + arr[0]
        temp1[1] = max(dp_mx) + arr[1]
        temp1[2] = max(dp_mx[1], dp_mx[2]) + arr[2]
        temp2[0] = min(dp_mn[0], dp_mn[1]) + arr[0]
        temp2[1] = min(dp_mn) + arr[1]
        temp2[2] = min(dp_mn[1], dp_mn[2]) + arr[2]
        dp_mx = temp1[:]
        dp_mn = temp2[:]
    print(max(dp_mx), min(dp_mn))
    return

main()
