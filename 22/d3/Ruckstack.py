
def charToInt(char):
    char = ord(char)
    if (char == 10):
        return None

    if (char < 97):
        char -= 38
    else:
        char -= 96
    return char


with open('./d3/input.txt', 'r') as reader:
    line = reader.readline()
    sum = 0
    while line != '':
        line = line.strip()

        half = int(len(line)/2)

        firstCompartment = []

        for i in range(half):
            firstCompartment.append(charToInt(line[i]))

        errFound = True
        for i in range(half, len(line)):

            if firstCompartment.__contains__(charToInt(line[i])):
                errFound = False
                sum += charToInt(line[i])
                break

        if (errFound):
            print(line)

        # print(firstCompartment)

        line = reader.readline()
    print(sum)
