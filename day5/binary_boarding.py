with open('input.txt', 'r') as f:
    entries = f.readlines()

highest = 0
seats = arr = [[0 for i in range(8)] for j in range(128)] 
ids = set()
for entry in entries:
    row = entry[:7]
    column = entry[7:]

    rows = list(range(128))

    for r in row:
        if r == 'F':
            rows = rows[:len(rows)//2]
        else:
            rows = rows[len(rows)//2:]
    
    columns = list(range(8))
    for c in column:
        if c == 'L':
            columns = columns[:len(columns)//2]
        else:
            columns = columns[len(columns)//2:]
    
    seats[int(rows[0])][int(columns[0])] = 1

    if int(rows[0]) * 8 + int(columns[0]) > highest:
        ids.add(int(rows[0]) * 8 + int(columns[0]))
        highest = int(rows[0]) *8 + int(columns[0])

print('The highest id is: ', highest)



