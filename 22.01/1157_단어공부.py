word = list(input())
temp = {}
many = ''
for i in word:
    i = i.upper()
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1

max_count = 0
max_letter = ''
for key, value in temp.items():
    if value > max_count:
        max_count = value
        max_letter = key
    elif value == max_count:
        max_letter = '?'

print(max_letter)
