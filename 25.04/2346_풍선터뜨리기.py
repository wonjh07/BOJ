from collections import deque
from sys import stdin
stdin = open('input.txt', 'rt')
input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dq = deque()
ans = []

for i in range(N):
    dq.append((nums[i], i+1))

while dq:
    num, idx = dq.popleft()
    ans.append(idx)

    if not dq:
        break

    if num > 0:
        dq.rotate(-(num - 1))
    else:
        dq.rotate(-num)

print(' '.join(map(str, ans)))

"""
이문제는 자바스크립트로 통과할 수 없습니다.
1등코드
def main():
    N = int(input())  # 카드의 개수 입력 받기
    cards = list(map(int, input().split()))  # 카드 값 입력 받기
    balloons = list(range(N))  # 카드 위치를 나타내는 리스트 생성
    ind = 0  # 현재 인덱스
    result = []

    while cards:
        result.append(balloons.pop(ind) + 1)  # 해당 카드의 원래 위치 기록
        mov = cards.pop(ind)  # 현재 위치의 이동 값

        if not cards:
            break

        if mov > 0:
            ind = (ind + mov - 1) % len(cards)
        else:
            ind = (ind + mov) % len(cards)

    print(" ".join(map(str, result)))  # 결과 출력

if __name__ == "__main__":
    main()
"""
