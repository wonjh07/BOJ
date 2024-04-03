word = list(input())
history = {}
for i in range(len(word)):
    if word[i] not in history:
        history[word[i]] = i

result = []
temp = ord('a')
while temp <= ord('z'):
    if chr(temp) in history:
        result.append(history[chr(temp)])
    else:
        result.append(-1)
    temp += 1
print(' '.join(map(str, result)))
