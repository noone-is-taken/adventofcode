"""
Day 7

Part 1

You quickly make a list of the horizontal position of each crab
(your puzzle input). Crab submarines have limited fuel, so you
need to find a way to make all of their horizontal positions 
match while requiring them to spend as little fuel as possible.


16,1,2,0,4,2,7,1,2,14

Each change of 1 step in horizontal position of a 
single crab costs 1 fuel. You could choose any 
horizontal position to align them all on, but the one 
that costs the least fuel is horizontal position 2:

Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel

This cost 37

The answer is 37 but what we need to find is the least fuel costing position.



Order positions and find the Median. 

Calculate fuel cost from the Median

Part 2

As it turns out, crab submarine engines don't burn fuel at a constant rate. 
Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than 
the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

Find the mean (mitjana) and calculate fuel from it

"""

def crabFuelCost(crabPos, destination):
    t = 0
    for x in range(abs(crabPos - destination) + 1):
        t += x
    return t


crabPositions = input('Insert Crabs Horizontal Position')

crabPositions = crabPositions.split(',')

crabPosInt = []

total = 0
for crabPos in crabPositions:
    crabPosInt.append(int(crabPos))
    total += int(crabPos)

#sort the list and get the Median
crabPosInt.sort()
#median
m = crabPosInt[int(len(crabPosInt)/2)]

#mean
mean = round(total / int(len(crabPosInt)))

fuel = 0

for crab in crabPosInt:
    fuel += crabFuelCost(crab,mean)

print(mean)
print(fuel)


