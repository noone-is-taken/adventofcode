#maping sistem! very complicado

#input:
#seeds: 79 14 55 13

#seeds to soil map:
#50 98 2
#52 50 48

#la primera linia basicament diu: del 98 canviarem a 50
#aixi que la sequencia seria:
#96    98
#97    99
#98    50
#99    51

file = open('./input_d.txt')


seeds = file.readline()
seeds_to_soil = []
soil_to_fert = []
fer_to_wat = []
water_to_light = []
light_to_temp = []
temp_to_hum = []

n_map = 0
for line in file:
    if line == '\n':
        n_map += 1
        file.readline()
        continue
    if n_map == 1:
        
        line = line.split(' ')
        line[-1] = line[-1].replace('\n','')
        print(line)
        mapp = [x for x in line if x != '']

        seeds_to_soil.append(mapp)


file.close()
print(seeds_to_soil)
