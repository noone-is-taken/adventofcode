
num_stacks = 9

with open("./d5/input.txt", "r") as reader:
    line = reader.readline()

    input = []
    for i in range(num_stacks):
        input.append([])

    while line != '' and line != '\n':

        for nstack in range(num_stacks):
            input[nstack].append(line[(nstack*4)+1])

        line = reader.readline()

    stacks = []
    for i in range(num_stacks):
        stacks.append([])

    for i in reversed(range(len(input[0]))):

        for n_stack in range(num_stacks):
            item = input[n_stack][i]
            if not (item.isnumeric()) and item != ' ':
                stacks[n_stack].append(item)

    line = reader.readline().strip()

    instructions = []

    while line != '':

        instructions.append(line)
        line = reader.readline().strip()


for instruc in instructions:
    instruc = instruc.split(" ")

    num_moves = int(instruc[1])
    stack_origin_index = int(instruc[3])-1
    stack_dest_index = int(instruc[5])-1

    tmp = []

    for i in range(num_moves):

        tmp.append(stacks[stack_origin_index].pop())

    # part 2
    tmp = reversed(tmp)

    for item in tmp:
        stacks[stack_dest_index].append(item)


for stack in stacks:
    print(stack.pop(), end='')
