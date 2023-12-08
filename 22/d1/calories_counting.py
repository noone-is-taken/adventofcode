# for code simplicity you should add extra cases in the default input (some extra breaklinees)
sum = 0
maxSum = 0
secondMax = 0
thirdMax = 0

with open("./input.txt", "r") as reader:
    line = reader.readline()
    while (line != ''):
        if line == '\n':
            if sum > maxSum:
                thirdMax = secondMax
                secondMax = maxSum
                maxSum = sum
            elif sum > secondMax:
                thirdMax = secondMax
                secondMax = sum
            elif sum > thirdMax:
                thirdMax = sum
            sum = 0
        else:
            sum += int(line)
        line = reader.readline()
    print(maxSum + secondMax + thirdMax)
