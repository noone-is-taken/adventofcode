f = open('input.txt')
instruction = f.readline()[:-1]
f.readline()

network = {}
for l in f:
    camps = l.replace(' ','')[:-1].split('=') 
    key = camps[0]
    values = camps[1].replace('(','').replace(')','').split(',')
    network[key] = values




current_node = 'AAA'
suma = 0
ins_index = 0
while(current_node != 'ZZZ'):
    act_inst = instruction[ins_index]
    ins_index += 1
    if ins_index == len(instruction):
        ins_index = 0
    if act_inst == 'R':
        current_node = network[current_node][1]
    elif act_inst == 'L':
        current_node = network[current_node][0]
    suma += 1

print(suma)
    
