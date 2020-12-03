from collections import Counter 
with open('input.txt', 'r') as f:
    entries = [s.split() for s in f.readlines()]

"""Part 1"""
valid_pass = 0
for password in entries:
    letter = password[1][0]
    p = Counter(password[2])
    if p[letter] in range(int(password[0].split('-')[0]), int(password[0].split('-')[1])+1):
        valid_pass += 1

print(f'Part 1: {valid_pass}')


"""Part 2"""
valid_pass = 0
for password in entries:
    first, second = password[0].split('-') 
    letter = password[1][0]
    if (password[2][int(first)-1] == letter) ^ (password[2][int(second)-1] == letter):
        valid_pass += 1  

print(f'Part 2: {valid_pass}')



