
def recus_encript(message, count, line):

    if len(message) == 4:
        return count + 1
    else:
        count += 1
        while message.__contains__(line[count]):
            message.pop(0)
        message.append(line[count])

        return recus_encript(message, count, line)


with open('./d6/input.txt', 'r') as reader:

    line = reader.readline().strip()

    message = []

    count = -1

    while len(message) != 14:

        count += 1
        while message.__contains__(line[count]):
            message.pop(0)
        message.append(line[count])

    print(count+1)

    # print(recus_encript(message, count, line))
