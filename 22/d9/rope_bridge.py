
instructions = []

with open('./d9/input.txt', 'r') as reader:
    line = reader.readline().strip()

    while line != '':

        direction, steps = line.split(' ')

        instructions.append((direction, int(steps)))
        line = reader.readline().strip()


map = []
map.append(['#'])

head_pos = [0, 0]
tail_pos = [0, 0]

head_last_pos = []

print(map)


def extMapR():
    for m in map:
        m.append('.')


def extMapD():
    map.append(['.']*len(map[0]))


def extMapU():
    map.insert(0, ['.']*len(map[0]))
    head_pos[0] += 1
    tail_pos[0] += 1
    for x in head_last_pos:
        x[0] += 1


def extMapL():
    for m in map:
        m.insert(0, '.')
    head_pos[1] += 1
    tail_pos[1] += 1
    for x in head_last_pos:
        x[1] += 1


def tail_follow():
    global tail_pos
    t = [head_pos[0], head_pos[1]]
    head_last_pos.append(t)

    if tail_pos[0] > head_pos[0]+1 or tail_pos[1] < head_pos[1] - 1 or tail_pos[0] < head_pos[0] - 1 or tail_pos[1] > head_pos[1] + 1:
        tail_pos = [head_last_pos[-2][0], head_last_pos[-2][1]]
        map[tail_pos[0]][tail_pos[1]] = '#'


for instruct in instructions:

    if instruct[0] == 'R':

        for steps in range(instruct[1]):
            if (head_pos[1] == len(map[0])-1):
                extMapR()
            # map[head_pos[0]][head_pos[1]] = '.'
            # map[head_pos[0]][head_pos[1] + 1] = 'H'
            head_pos[1] += 1

            tail_follow()

            # if tail_pos[1]+1 < head_pos[1]:
            #     tail_pos[1] += 1
            #     if tail_pos[0] != head_pos[0]:
            #         tail_pos[0] = head_pos[0]

    elif instruct[0] == 'L':
        for steps in range(instruct[1]):
            if head_pos[1] == 0:
                extMapL()
            # map[head_pos[0]][head_pos[1]] = '.'
            # map[head_pos[0]][head_pos[1] - 1] = 'H'
            head_pos[1] -= 1

            tail_follow()
            # if tail_pos[1]-1 > head_pos[1]:
            #     tail_pos[1] -= 1
            #     if tail_pos[0] != head_pos[0]:
            #         tail_pos[0] = head_pos[0]
    elif instruct[0] == 'D':
        for steps in range(instruct[1]):
            if head_pos[0] == len(map)-1:
                extMapD()
            # map[head_pos[0]][head_pos[1]] = '.'
            # map[head_pos[0]+1][head_pos[1]] = 'H'
            head_pos[0] += 1

            tail_follow()
            # if tail_pos[0]+1 > head_pos[0]:
            #     tail_pos[0] += 1
            #     if tail_pos[1] != head_pos[1]:
            #         tail_pos[1] = head_pos[1]
    elif instruct[0] == 'U':
        for steps in range(instruct[1]):
            if head_pos[0] == 0:
                extMapU()
            # map[head_pos[0]][head_pos[1]] = '.'
            # map[head_pos[0]-1][head_pos[1]] = 'H'
            head_pos[0] -= 1

            tail_follow()
            # if tail_pos[0]-1 < head_pos[0]:
            #     tail_pos[0] -= 1
            #     if tail_pos[1] != head_pos[1]:
            #         tail_pos[1] = head_pos[1]

    # map[tail_pos[0]][tail_pos[1]] = '#'

    # for line in map:
    #     for p in line:
    #         print(p, end='')
    #     print('')
    # print('next map')

sum = 0
for l in map:
    for i in l:
        if i == '#':
            sum += 1

print(sum)
