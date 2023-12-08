#maping sistem! very complicado

#input:
#seeds: 79 14 55 13

#seeds to soil map:
#50 98 2
#52 50 48

#la primera linia basicament diu: del 98 canviarem a 50
#aixi que la sequencia seria:
#96    98
#97    99
#98    50
#99    51

file = open('./input.txt')

data = []
for line in file:
    line = line.split(' ')
    res = {}
    res['source_start'] = line[1]
    res['length'] = line[2]

    data.append(res)

source_map = {}

for line in data:
    for x in range(line['source_start'], line['source_start']+line['length']):
        if x in source_map:
            print('choque')
        source_map[x] = 1
