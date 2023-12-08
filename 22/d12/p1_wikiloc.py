
mapa = []
start = -1
end = -1
row_count = 0
colum_count = 0
with open('./d12/input.txt', 'r') as reader:
    line = reader.readline()

    while line != '':
        row = []
        colum_count = 0
        for c in line:
            if c == 'S':
                start = [row_count, colum_count]
            elif c == 'E':
                end = [row_count, colum_count]
            row.append(c)
            colum_count += 1

        row_count += 1
        mapa.append(row)

        line = reader.readline()

position = start


while position != end:

    rest = [abs(position[0] - end[0]), abs(position[1] - end[1])]

    if rest[0] == rest[1]:
        position[0] += 1
    elif rest[0] > rest[1]:
        position[0] += 1
    elif rest[0] < rest[1]:
        position[1] += 1


print(mapa)
