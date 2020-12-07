with open('input.txt', 'r') as f:
    line = f.read().replace('.', '').replace('bags', '').replace('bag','')
    entries = {l.split('contain ')[0].rstrip(): [s.rstrip() for s in l.split('contain ')[1].split(', ')] for l in line.split('\n')}

for e in entries:
    temp = {}
    for i, val in enumerate(entries[e]):
        if val == 'no other':
            temp = {'no other': 0}
            continue
        temp[val[2:len(val)]] = int(val[:1])
    entries[e] = temp

val = set()

def find_bag(bag):
    global val
    if bag == 'no other':
        return False

    if bag == 'shiny gold':
        return True
    
    
    contained = entries[bag]
    
    foo = False
    for b in contained:
        temp = find_bag(b)
        if temp:
            foo = temp
    return foo

l = [] 
for b, items in entries.items():
    if b != 'shiny gold':
        l.append(find_bag(b))

#print(sum(l))


def count_bags(bag, num):
    if bag == 'no other':
        return 0
    
    curr_sum = 0
    for bag, val in entries[bag].items():
        curr_sum += val + val * count_bags(bag, num)
    
    return curr_sum



print(count_bags('shiny gold', 0))