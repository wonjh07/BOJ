import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def main():
    N, S = map(int, input().rstrip().split())
    mn, ans, cnt = 0, 0, 0
    e = 0
    arr = list(map(int, input().rstrip().split()))
    for i in range(N):
        if arr[i] >= S:
            print(1)
            return
        ans += arr[i]
        cnt += 1
        if ans >= S:
            e = i
            mn = cnt
            break
            
    if not mn:
        print(0)
        return

    for j in range(1, N):
        ans -= arr[j-1]
        cnt -= 1
        if S > ans and e < N-1:
            e += 1
            if arr[e] >= S:
                print(1)
                return
            ans += arr[e]
            cnt += 1
        else:
            while 1:
                if ans - arr[e] < S:
                    break
                ans -= arr[e]
                cnt -= 1
                e -= 1
        if S <= ans and mn > cnt:
            mn = cnt

    print(mn)
    return
main()

