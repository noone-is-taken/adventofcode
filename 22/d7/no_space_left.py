
reader = open('./d7/input.txt', 'r')


def no_space_recursive(dirname, sum, reader):
    line = reader.readline().strip()
    if line == '$ cd ..':
        return sum
    else:
        firstParam = line.split(' ')[0]
        if line == '$ ls':
            line = reader.readline().strip()
            firstParam = line.split(' ')[0]
            while firstParam != '$':
                if (firstParam.isnumeric()):
                    sum += int(firstParam)
                line = reader.readline().strip()
                firstParam = line.split(' ')[0]
        if line.__contains__('$ cd '):
            dirName = line.split(' ')[2]
        no_space_recursive(dirName, sum, reader)


no_space_recursive('', 0, reader)
