
trees = []

with open('./d8/input.txt', 'r') as reader:
    line = reader.readline().strip()

    while line != '':

        chars = []

        for c in line:
            chars.append(int(c))

        # trees.append([*line])
        trees.append(chars)

        line = reader.readline().strip()


width = len(trees[0])
height = len(trees)

sum = 0
MaxSum = 0


for h, treesline in enumerate(trees):
    if (h != 0 and h != height-1):
        for w, tree in enumerate(treesline):
            if (w != 0 and w != width-1):
                # print(tree, end='')
                # part 1
                TopVisible = True
                LeftVisible = True
                RightVisible = True
                DownVisible = True
                # Note
                # part 2
                TopSum = 0
                LeftSum = 0
                RighSum = 0
                DownSum = 0

                for i in reversed(range(0, h)):
                    if trees[i][w] >= tree:
                        TopSum += 1
                        TopVisible = False
                        break
                    else:
                        TopSum += 1

                for i in reversed(range(0, w)):
                    if trees[h][i] >= tree:
                        LeftSum += 1
                        LeftVisible = False
                        break
                    else:
                        LeftSum += 1
                for i in range(w+1, width):
                    if trees[h][i] >= tree:
                        RighSum += 1
                        RightVisible = False
                        break
                    else:
                        RighSum += 1

                for i in range(h+1, height):
                    if trees[i][w] >= tree:
                        DownSum += 1
                        DownVisible = False
                        break
                    else:
                        DownSum += 1

                if DownVisible or TopVisible or LeftVisible or RightVisible:
                    sum += 1
                TotalSum = TopSum * LeftSum * RighSum * DownSum
                if TotalSum > MaxSum:
                    MaxSum = TotalSum
                # if trees[h-1][w] < tree or trees[h][w+1] < tree or trees[h+1][w] < tree or trees[h][w-1] < tree:
                #     sum += 1
            else:
                sum += 1
        # print('')
    else:
        sum += height


print(sum)
print(MaxSum)
