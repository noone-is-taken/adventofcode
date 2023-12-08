# data expected as ['asdasdas','aaasdada','asdasd']

data = []


f = open('./input.txt','r')
for line in f:
   data.append(line)

f.close()


#process data to change one -> 1 ; two -> 2 ; .... ; nine -> 9
new_data = []
for line in data:
    new_line = line.replace('one','o1e').replace('two','t2o').replace('three','t3e').replace('four','f4r').replace('five','f5e')
    new_line = new_line.replace('six','s6x').replace('seven','s7n').replace('eight','e8t').replace('nine','n9e')
    new_data.append(new_line)


total_sum = 0
for row in new_data:
     fn = ''
     for l in row:
         try:
             n = int(l)
             fn = fn + l
         except:
             print('', end='')
     fn = fn[0]+fn[-1]
     total_sum += int(fn)

print(total_sum)

