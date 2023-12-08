from functools import reduce
file = open('./input.txt')

data = []

real_cubes = {
        'red':12,
        'green':13,
        'blue':14,
        }
correct_games = 0
for line in file:
    
    filds = line.split(':')
    
    n_game = filds[0]

    cubes = filds[1].replace(';',',').replace('\n','').split(',')
    res = {}
    for cub in cubes:
        
        color = cub.split(' ')[2]
        number = int(cub.split(' ')[1])

        #res[color] = res[color] + number if color in res else number
        if not color in res:
            res[color] = number
        else:
            res[color] = number if res[color] < number else res[color]
   

    result = reduce((lambda x, y: x * y),res.values())
    correct_games = correct_games + result


print(correct_games)
file.close()

        

