
file = open('./input.txt')

def find_char(p):
    return '-' in p or '7' in p or '|' in p or 'L' in p or 'J' in p or 'F' in p

def find_next_pos(map,pos)->[int,int]:
    if pos[0] != 0:
        p = map[pos[0]-1][pos[1]]
        if find_char(p):
            return [pos[0]-1, pos[1]]
    if pos[1] != 0:
        p = map[pos[0]][pos[1]-1]
        if find_char(p):
            return [pos[0], pos[1]-1]
    if pos[0] != len(map[0])-1:
        p = map[pos[0]+1][pos[1]]
        if find_char(p):
            return [pos[0]+1, pos[1]]
    if pos[1] != len(map[1])-1:
        p = map[pos[0]][pos[1]+1]
        if find_char(p):
            return [pos[0], pos[1]+1]
    return [None,None]

map = [] #0 -> row 1 -> col
pos = [0,0]
start_pos = [None,None]
for line in file:
    pos[1] = 0
    line = line[:-1]
    map_line = []
    for char in line:
        if char == 'S':
            start_pos = [pos[0],pos[1]]
            char = 0
        map_line.append(char)
        pos[1] += 1
    pos[0] += 1
    map.append(map_line)


next_pos = find_next_pos(map,start_pos)
last_pos = [start_pos[0], start_pos[1]]
count = 1
while(map[next_pos[0]][next_pos[1]] != 0):
    pipe = map[next_pos[0]][next_pos[1]] 
    map[next_pos[0]][next_pos[1]] = count
    count += 1
    if last_pos[0] == next_pos[0]:
        #significa que coincideix la row
        if pipe == 'J' or pipe == 'L':
            #print('pujem')
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0]-1,next_pos[1]]
        elif pipe == 'F' or pipe == '7':
            #print('baixem')
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0]+1,next_pos[1]]
        elif pipe == '-':
            #print('dreta o esquerra')
            if next_pos[1] > last_pos[1]:
                dir = 1
            else:
                dir = -1 
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0], next_pos[1]+dir]
    elif last_pos[1] == next_pos[1]:
        #significa que coincideix la row
        if pipe == 'J' or pipe == '7':
            #print('esquerra')
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0],next_pos[1]-1]
        elif pipe == 'F' or pipe == 'L':
            #dreta
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0],next_pos[1]+1]
        elif pipe == '|':
            #print('abaix o adalt')
            if next_pos[0] > last_pos[0]:
                dir = 1
            else:
                dir = -1
            last_pos = [next_pos[0],next_pos[1]]
            next_pos = [next_pos[0]+dir, next_pos[1]]

print(count/2)


