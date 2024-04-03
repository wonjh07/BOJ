croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia:
    word = word.replace(str(i), '*')
print(len(word))
