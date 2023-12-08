



# get input
width, height = 5, 5
first_line = True
boards = []
board = []
i = -1
inMatrix = False

finall_win_n:int = None
finall_board = None
with open("./in.txt", "r") as reader:
    line = reader.readline()
    while line != '':
        if first_line:
            win_nums = []
            nums = line.split(',')
            for n in nums:
                try:
                    nint = int(n)
                    win_nums.append(nint)
                except:
                    pass
            first_line = False
        else:
            if line == '\n':
                if board.__len__() > 0:
                    boards.append(board)
                board = []
            else:
                nums = line.split(' ')
                line = []
                for n in nums:
                    try:
                        nint = int(n)
                        line.append(nint)
                    except:
                        pass
                board.append(line) 

        line = reader.readline()

    if board.__len__() > 0:
        boards.append(board)
line_complete = False
for win_n in win_nums:
    for boardIndx in range(boards.__len__()):
        board = boards[boardIndx]
        for line in board:
            for i in range(line.__len__()):
                if line[i] == win_n:
                    line[i] = 'x'
                    line_complete= True
                    for x in line:
                        if x != 'x':
                            line_complete = False
                            break
                    if not(line_complete):
                        line_complete = True
                        for l in board:
                            if l[i] != 'x':
                                line_complete = False
                                break
                    #if the column or the row was a complete line win
                    if line_complete:
                        # finall_board = boards.pop(boardIndx)
                        finall_board = boards[boardIndx]
                        boards[boardIndx] = []
                        finall_win_n = win_n
                        #for better performans here should check if boards are empty
                        break

sum = 0
for line in finall_board:
    for n in line:
        if n != 'x':
            sum += n

print(finall_win_n * sum)

