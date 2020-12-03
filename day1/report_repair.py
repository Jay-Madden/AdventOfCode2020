with open('input.txt', 'r') as f:
    entries = [int(s) for s in f.readlines()]

entries.sort()

i = 0
j = len(entries) -1
r = 0

s = False

for i, ival in enumerate(entries):
    for j, jval in enumerate(entries):
        for k, kval in enumerate(entries):
            if i == j or j == k or k == i:
                continue
            
            if ival + jval + kval == 2020:
                print(f'result found {ival*jval*kval}')
        


print(entries)
