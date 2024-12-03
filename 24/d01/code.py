nl = """3   4
4   3
2   5
1   3
3   9
3   3"""

nl = nl.split('\n')
l = []
r = []
res1 = 0
res2 = 0

for line in nl:
    line = line.split('   ')
    
    l.append(int(line[0]))
    r.append(int(line[1]))

# Only needed for part 1
l.sort()
r.sort()

for x in range(len(l)):
    res1 += abs(l[x]-r[x])
    res2 += l.count(r[x]) * r[x]
 

print(res1)
print(res2)
