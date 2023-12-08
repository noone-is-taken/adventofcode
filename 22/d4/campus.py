with open('./d4/input.txt', 'r') as reader:
    line = reader.readline().strip()
    sum = 0

    sumpart2 = 0

    while line != '':

        sections = line.split(',')

        sections[0] = sections[0].split('-')
        sections[1] = sections[1].split('-')

        # part 1

        if (int(sections[0][0]) >= int(sections[1][0]) and int(sections[0][1]) <= int(sections[1][1])):
            sum += 1
        elif (int(sections[0][0]) <= int(sections[1][0])):
            if (int(sections[0][1]) >= int(sections[1][1])):
                sum += 1

        # part 2

        if not (sections[0][1] > sections[1][0] or sections[1][1] > sections[0][0]):
            sumpart2 += 0

        if line == '8-56,8-8':
            print("wati")
        mesGran = sections[0][1]
        if int(sections[1][1]) > int(sections[0][1]):
            mesGran = sections[1][1]

        tmp = [0] * (int(mesGran) + 1)
        for i in range(int(sections[0][0]), int(sections[0][1])):
            tmp[i] += 1
        for i in range(int(sections[1][0]), int(sections[1][1])):
            tmp[i] += 1

        if (tmp.__contains__(2)):
            sumpart2 += 1

        line = reader.readline().strip()
    print(sumpart2)
