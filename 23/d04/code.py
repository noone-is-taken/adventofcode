f = open('./input.txt', 'r')

sum = 0
for l in f:
    numbers = l.split(':')[1].split('|')

    wining_numbers = numbers[0].split(' ')
    wining_numbers = [x for x in wining_numbers if x != '']

    card_numbers = numbers[1].split(' ')
    card_numbers = [x for x in card_numbers if x != '']
    card_numbers[-1] = card_numbers[-1].replace('\n','')
    

    count = 0
    for wining_num in wining_numbers:
        if wining_num in card_numbers:
            count = count + 1
    res = count
    if res != 0:
        res = 2 ** (res-1)
    sum = sum + res
        
print(sum) 
