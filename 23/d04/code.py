f = open('./input.txt', 'r')

sum = 0
for l in f:
    numbers = l.split(':')[1].split('|')

    wining_numbers = numbers[0].split(' ')
    del wining_numbers[0]
    del wining_numbers[-1]
    card_numbers = numbers[1].split(' ')
    del card_numbers[0]
    del card_numbers[-1]
    

    count = 0
    for wining_num in wining_numbers:
        if wining_num in card_numbers:
            count = count + 1
    if count > 2:
        res = 1
        #count = 2 ** (count-1)
        print(count)
        for x in range(count):
            res = res * 2
    sum = sum + count
        
print(sum) 
