f = open('./input.txt', 'r')

sum = 0
cards = {}
for l in f:
    card_key = int(l.split(':')[0].split(' ')[-1])
    numbers = l.split(':')[1].split('|')

    wining_numbers = numbers[0].split(' ')
    wining_numbers = [x for x in wining_numbers if x != '']

    card_numbers = numbers[1].split(' ')
    card_numbers = [x for x in card_numbers if x != '']
    card_numbers[-1] = card_numbers[-1].replace('\n','')

    

    count = card_key
    extra_cards = []
    for wining_num in wining_numbers:
        if wining_num in card_numbers:
            count = count + 1
            extra_cards.append(count)
    cards[card_key] = extra_cards
        
#print(cards) 
count = 0
space =  ''
def recursive_sum_cards(cards, actual_card, result, space):
    result[0] += 1 
    space += ' '
    for card in cards[actual_card]:
        #print(space + str(card))
        
        recursive_sum_cards(cards,card,result,space)
res = [0]
for card in cards.keys():
    recursive_sum_cards(cards, card, res, space)
print(res[0])
        
