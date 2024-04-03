def check_prime(num):
    if num in (2, 3, 5):
        return True
    elif num == 1:
        return False
    else:
        if num % 2 == 0:
            return False
        for x in range(3, num // 2 + 1, 2):
            if num % x == 0:
                return False
        return True


case = int(input())
count = 0
nums = map(int, input().split())
for i in nums:
    if check_prime(i):
        count += 1
print(count)
