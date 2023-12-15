maps = {}
current_map = ''
maps_order = []
for line in open('input.txt'):
    if line == '\n':
        continue
    if ':' in line:
        line = line.split(':')
        if line[0] == 'seeds':
            seeds = [int(x) for x in line[1][1:].split(' ')]
           # group1 = [x for x in range(seeds[0],seeds[0]+seeds[1])]
           # group2 = [x for x in range(seeds[2],seeds[2]+seeds[3])]
           # seeds = group1 + group2
        elif 'map' in line[0]:
            current_map = line[0].split(' ')[0]
            maps_order.append(current_map)
        else:
            maps[current_map] = numbers

    else:
        numbers = [int(x) for x in line.split(' ')]
        if current_map not in maps:
            maps[current_map] = []
        maps[current_map].append(numbers)
print(seeds)
seed_result = []
for seed in seeds:
    targ = seed
    for index_map in range(len(maps)):
        for line in maps[maps_order[index_map]]:
            if targ >= line[1] and targ <= line[1]+line[2]:
                targ = targ + line[0] - line[1]
                break
        #print(maps_order[index_map]+' '+str(targ))
    seed_result.append(targ)

print(min(seed_result))
