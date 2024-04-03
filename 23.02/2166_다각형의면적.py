import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N = int(input().rstrip())
    res = 0
    ry, rx = map(int, input().rstrip().split())
    y1, x1 = ry, rx
    for _ in range(N-1):
        y2, x2= map(int, input().rstrip().split())
        res += x1 * y2 - y1 * x2
        y1, x1 = y2, x2
    res += x1 * ry - y1 * rx
    print(round(abs(res)/2, 1))
    return
main()