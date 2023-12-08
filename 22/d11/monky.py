from numpy import *


class Monky:

    def __init__(self, v_start_items, v_operation, v_test, v_true_m, v_false_m) -> None:
        self.start_items = array(v_start_items)
        self.operation = v_operation
        self.test = v_test
        self.true = v_true_m
        self.false = v_false_m
        self.inspection = 0


monkys = []
monky_info = []

with open('./d11/input.txt', 'r') as reader:

    line = reader.readline()

    while line != '':

        if line == '\n':
            items = [int(num_s)
                     for num_s in monky_info[1].split(':')[1].split(',')]
            operation = monky_info[2].split(':')[1]
            test = int(monky_info[3].split('by')[1])
            m_true = int(monky_info[4].split('monkey')[1])
            m_fals = int(monky_info[5].split('monkey')[1])

            m = Monky(items, operation, test, m_true, m_fals)
            monkys.append(m)
            monky_info = []

        if line != '\n':
            monky_info.append(line)

        line = reader.readline()

print(monkys)


for x in range(10000):
    for monky in monkys:
        monky_items = monky.start_items.view()
        for i, item in enumerate(monky.start_items):
            monky.inspection += 1
            result = int(item)
            monky_items = delete(monky_items, 0)

            if monky.operation.__contains__("+"):
                #   +
                op = monky.operation.split("=")[1]
                num = op.split("+")[1].strip()
                if num.isnumeric():
                    result = result + int(num)
                else:
                    result = result + result
            else:
                #   *
                op = monky.operation.split("=")[1]
                num = op.split("*")[1].strip()
                if num.isnumeric():
                    result = result * int(num)
                else:
                    result = result * result

            #result = result // 3

            if result % monky.test == 0:
                monkys[monky.true].start_items = append(
                    monkys[monky.true].start_items, result)
            else:
                monkys[monky.false].start_items = append(
                    monkys[monky.false].start_items, result)
                # monkys[monky.false].start_items.append(result)
        monky.start_items = monky_items


big = 0
second_big = 0
for monky in monkys:
    if monky.inspection > big:
        second_big = big
        big = monky.inspection
    elif monky.inspection > second_big:
        second_big = monky.inspection
    print(monky.inspection)

print("AAAAA")
print(big * second_big)
