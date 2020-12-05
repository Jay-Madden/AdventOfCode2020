import re
with open('input.txt', 'r') as f:
    entries = f.read()

def part1(entries):
    fields1 = ['byr','iyr','eyr', 'ecl', 'hgt','hcl','pid']
    entries = [{e.split(':')[0]:e.split(':')[1] for e in p.split()} for p in entries.split('\n\n')]
    valid_pass = sum([all(f in entry for f in fields1) for entry in entries])

    print(valid_pass)


def part2(entries):
    fields1 = {
        'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
        'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
        'eyr': lambda s: len(s) == 4 and 2020 <= int(s) <= 2030, 
        'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
        'hgt': lambda s: ('cm' in s and 150 <= int(s.replace('cm', '')) <= 193) or('in' in s and 59 <= int(s.replace('in', ''))  <= 76),
        'hcl': lambda s: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', s) != None,
        'pid': lambda s: len(s) == 9,
    }

    entries = [{e.split(':')[0]:e.split(':')[1] for e in p.split()} for p in entries.split('\n\n')]
    correct_fields = [z for z in [entry if all(f in entry for f in fields1) else None for entry in entries] if z is not None]
    valid_pass = sum([all([fields1.get(k, lambda s: True)(v) for k,v in passports.items()]) for passports in correct_fields])
    print(valid_pass)

part2(entries)