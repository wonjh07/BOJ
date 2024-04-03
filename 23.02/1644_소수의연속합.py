import sys
input = sys.stdin.readline

def main():
    N = int(input())
    if N == 1:
        print(0)
        return

    # 에라토스테네스 체 소수찾기
    def find_prime():
        nums = [1] * (N+1)
        for i in range(3, int(N ** 0.5) + 1, 2):
            idx = i ** 2
            while idx <= N:
                nums[idx] = 0
                idx += i
        temp = [2]
        for i in range(3, N+1, 2):
            if nums[i]:
                temp.append(i)
        return temp

    primes = find_prime()
    last_i = len(primes)-1
    ans, cnt, s, e = 2, 0, 0, 0
    while 1:
        # 뒷 포인터 옮기기
        while e < last_i:
            if ans >= N:
                break
            e += 1
            ans += primes[e]
        # 부분합이 N일경우 cnt 1 증가
        if ans == N:
            cnt += 1
        if e == last_i and s == e:
            break
        #앞포인터 앞으로 한칸옮기기
        if s < e:
            ans -= primes[s]
            s += 1
        #뒷포인터 앞으로 옮기기
        while s < e:
            if ans <= N:
                break
            ans -= primes[e]
            e -= 1
    print(cnt)
    return
main()