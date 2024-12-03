inpu = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
reports = inpu.split('\n')
r = []
for level in reports:
    r.append([int(x) for x in level.split(' ')])

res = 0
for l in r:
    i = 0
    safe = True
    first_safe = True
    asc = l[i] < l[i+1]
    des = l[i] > l[i+1]
    while safe and i < len(l)-1:
        if asc:
            safe = l[i] < l[i+1]
        else:
            safe = l[i] > l[i+1]

        if safe:
            safe = abs(l[i]-l[i+1]) <= 3

        if not safe:
            if i < len(l)-2:
                if asc:
                    safe = l[i] < l[i+2]
                elif des:
                    safe = l[i] > l[i+2]
                if safe:
                    safe = abs(l[i]-l[i+2]) <= 3

            if not safe:
                break;
        i=i+1

    if safe:
        print(l)
        res += 1

print(res)
