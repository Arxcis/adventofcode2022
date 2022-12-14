import fileinput, re
from dataclasses import dataclass
from functools import reduce

@dataclass
class Operation:
    left: str
    operand: str
    right: str

@dataclass
class Monkey:
    id: int
    items: list[int]
    operation: Operation
    divisible_by: int
    if_true: int
    if_false: int
    inspect_count: int

"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

filetext = " ".join([line for line in fileinput.input()])

#
# Parse input
#
def make_monkeys():
    return [Monkey(
        id=int(id),
        items=[int(part) for part in re.findall("\d+", starting)],
        operation=Operation(left=left,operand=operand,right=right),
        divisible_by=int(divisible_by),
        if_true=int(if_true),
        if_false=int(if_false),
        inspect_count=0
    ) for id, starting, left, operand, right, divisible_by, if_true, if_false in re.findall(
        "Monkey (\d+):\s+"+
            "Starting items: ([\d,\s]+)\s+"+
            "Operation: new = (old) (\*|\+) (old|\d+)\s+"+
            "Test: divisible by (\d+)\s+"+
                "If true: throw to monkey (\d+)\s+"+
                "If false: throw to monkey (\d+)", 
        filetext
    )]


def calculate_worry_level(monkey, item):
    if monkey.operation.operand == "*":
        if monkey.operation.right == "old":
            return item * item
        else:
            return item * int(monkey.operation.right)

    else: # monkey.operation.operand == "+"
        if monkey.operation.right == "old":
            return item + item
        else:
            return item + int(monkey.operation.right)


#
# ----------- Part 1 ---------------
#
monkeys = make_monkeys()

for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            worry_level: int = calculate_worry_level(monkey, item)
            
            worry_level //= 3

            if worry_level % monkey.divisible_by == 0:
                monkeys[monkey.if_true].items.append(worry_level)
            else:
                monkeys[monkey.if_false].items.append(worry_level)
        
        monkey.inspect_count += len(monkey.items)
        monkey.items = [] # All items thrown away to other monkeys

sorted = [monkey.inspect_count for monkey in monkeys]
sorted.sort(reverse=True)
print(reduce(lambda a, b: a*b, sorted[:2]))

#
# ----------- Part 2 ---------------
#
monkeys = make_monkeys()

common_multiple = reduce(lambda a,b: a*b, [m.divisible_by for m in monkeys])

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            worry_level: int = calculate_worry_level(monkey, item)
             
            worry_level %= common_multiple
            
            if worry_level % monkey.divisible_by == 0:
                monkeys[monkey.if_true].items.append(worry_level)
            else:
                monkeys[monkey.if_false].items.append(worry_level)
        
        monkey.inspect_count += len(monkey.items)
        monkey.items = [] # All items thrown away to other monkeys

sorted = [monkey.inspect_count for monkey in monkeys]
sorted.sort(reverse=True)
print(reduce(lambda a, b: a*b, sorted[:2]))
