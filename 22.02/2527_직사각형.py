import sys
input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().rstrip().split())
    # 사각형 1 중심
    ct1 = [(p1 + x1) / 2, (q1 + y1) / 2]
    # 사각형 2 중심
    ct2 = [(p2 + x2) / 2, (q2 + y2) / 2]
    # 사각형 1 중심에서 x축, y축
    w1 = (p1 - x1) / 2
    h1 = (q1 - y1) / 2
    # 사각형 2 중심에서 x축, y축
    w2 = (p2 - x2) / 2
    h2 = (q2 - y2) / 2
    # 사각형 1,2 의 중심사이 거리
    cx = abs(ct1[0] - ct2[0])
    cy = abs(ct1[1] - ct2[1])
    # 사각형 1기준으로 사각형 2가 그리는 중심선이 최소 접할때
    if w1 + w2 >= cx and h1 + h2 >= cy:
        # 꼭지점에서 만날때
        if w1 + w2 == cx and h1 + h2 == cy:
            print('c')
        # 직선에서 만날때
        elif w1 + w2 == cx or h1 + h2 == cy:
            print('b')
        #그외에는 직사각형
        else:
            print('a')
    # 사각형이 어떠한 접점도 없음
    else:
        print('d')