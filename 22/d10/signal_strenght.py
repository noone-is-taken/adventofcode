
x = 1
c = 0
v = 0

addxExecuting = False
totalSum = 0

with open('./d10/input.txt', 'r') as reader:
    line = reader.readline().strip()

    while line != '':
        c += 1

        if c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220:
            totalSum += (c * x)
            print(c * x)

        if addxExecuting:
            x += v
            line = reader.readline().strip()
            while line.__contains__('noop'):
                line = reader.readline().strip()
                c += 1
                if c == 20 or c == 60 or c == 100 or c == 140 or c == 180 or c == 220:
                    totalSum += (c * x)

        if not (addxExecuting):
            addxExecuting = True
            v = int(line.split(' ')[1])
        else:
            addxExecuting = False

        if c == 220:
            break

        print('x value is ' + str(x) + ' in the cycle ' + str(c))

    # if v != 0:
    #     c += 1
    #     x += v
    #     print('x value is ' + str(x) + ' in the cycle ' + str(c))

print(totalSum)
