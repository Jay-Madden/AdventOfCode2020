from collections import Counter
with open('input.txt', 'r') as f:
    entries = [e.split() for e in f.read().split('\n\n')]

"""part1"""
num = 0
for e in entries:
    local_set = set()
    for l in e:
        local_set = local_set | set(l)
    num += len(local_set)

"""part2"""
num = 0
for e in entries:
    temp =0 
    l = len(e)
    j = ''.join(e)
    count = Counter(j)
    for c in ''.join(set(j)):
        if count[c] == l:
            temp += 1
    num+=temp

print(num)
