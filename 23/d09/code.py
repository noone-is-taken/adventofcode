def all_zero(arr):
    for x in arr:
        if x != 0:
            return False
    return True

f = open('input.txt')
input_historys = []
for l in f:
    input_historys.append([int(x) for x in l.split(' ')])
result = 0
for history in input_historys:
    diff = []
    res = 0
    while(not all_zero(history)):
        diff = []
        for x in range(len(history)-1):
            diff.append(history[x+1]-history[x])

        
        res += history[-1]
        history = diff
    
    result += res

print(result)
