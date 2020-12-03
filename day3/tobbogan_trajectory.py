from functools import reduce
with open('input.txt', 'r') as f:
    entries = [s[:-1] for s in f.readlines()]
    entries = [s*len(entries) for s in entries]
states = [(3,1),(1,1),(5,1),(7,1),(1,2)]

for s_i, (j_step, i_step) in enumerate(states):
    results = {".": 0, "#": 0 }
    i = i_step
    j = j_step
    while i < len(entries):
        results[entries[i][j]] += 1
        i += i_step
        j += j_step
    states[s_i] = results['#']

print(reduce(lambda x,y: x*y, states))
