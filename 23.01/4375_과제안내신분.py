# sub = []
# sub_min = [0] * 30


# for i in range(0, 28):
#     a = int(input())
#     sub.append(a)
# sub.sort(reverse=False)

# for i in range(0, len(sub)):
#     if sub[i] == i+1:
#         sub_min[i] == 0
#     else:
#         sub_min[i] == 1
# print(sub_min)

from sys import stdin as s
s = open("input.txt", "rt") # 제출할때만 이부분을 지워주면 됨

cnt = 0
ans = []
check = [0] * 31  # 인덱스 0번째 0번학생은 존재 x 0은 비워두고 1~30 인덱스만큼의 0만 사용
sub = [int(s.readline().rstrip()) for _ in range(28)]

# 받아온 명단을 check 리스트에 기록
for i in sub:
    check[i] += 1

# check 리스트에서 가장처음으로 0을 발견하면 그요소의 인덱스가 곧 학생 번호
# 처음, 두번째 0 인 학생을 발견하면 ans에 append 하고 탐색을 종료
for j in range(1, len(check)):
    if check[j] == 0:
        ans.append(j)
        cnt += 1
    if cnt == 2:
        break

print(*ans, sep='\n')
