

with open("./input.txt", "r") as reader:
    line = reader.readline()
    sum = 0
    while (line != ''):
        choses = line.strip().split(" ")
        winSum = 3

        if (choses[0] == "A"):
            if (choses[1] == "Z"):
                winSum = 0
            elif (choses[1] == "Y"):
                winSum = 6
        elif (choses[0] == "B"):
            if (choses[1] == "X"):
                winSum = 0
            elif (choses[1] == "Z"):
                winSum = 6
        elif (choses[0] == "C"):
            if (choses[1] == "Y"):
                winSum = 0
            elif (choses[1] == "X"):
                winSum = 6

        chosesSum = 1
        if (choses[1] == "Y"):
            chosesSum = 2
        elif (choses[1] == "Z"):
            chosesSum = 3

        sum += chosesSum + winSum

        line = reader.readline()

    print(sum)
