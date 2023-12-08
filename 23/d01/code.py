# data expected as ['asdasdas','aaasdada','asdasd']
total_sum = 0
for c in r:
     fn = ''
     for l in c:
         try:
             n = int(l)
             fn = fn + l
         except:
         print('', end='')
     fn = fn[0]+fn[-1]
     total_sum += int(fn)

