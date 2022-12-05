import fileinput
import re

#
# ---------- PARSE INPUT ------------
#
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

procedure = []
stack_lines = []
for line in fileinput.input():
    if "[" in line:
        """
        ['   ', '[D]', '   ']
        ['[N]', '[C]', '   ']
        ['[Z]', '[M]', '[P]']
        """
        parts = re.findall("(\s\s\s|\[\w\])\s", line)
        stack_lines.append(parts)    
    
    elif "move" in line:
        Move, From, To = re.findall("move (\d+) from (\d+) to (\d+)", line)[0]
        procedure.append((int(Move), int(From), int(To)))


def make_stacks():
    stacks = [[] for i in range(len(stack_lines[0]))]

    # Reverse traversal, from bottom and up the stacks
    for line in stack_lines[-1::-1]:
        for i, crate in enumerate(line):
            if "[" in crate:
                stacks[i].append(crate)
    return stacks
#
# --------- PART 1 ------------
#
stacks = make_stacks()

for Move, From, To in procedure:
    for _ in range(Move):
        crate = stacks[From - 1].pop()
        stacks[To - 1].append(crate) 
    

print("".join([stack[-1].replace("[","").replace("]","") for stack in stacks]))

#
# --------- PART 2 --------------
#
stacks = make_stacks()

for Move, From, To in procedure:
    crates = [stacks[From - 1].pop() for _ in range(Move)]
    stacks[To - 1].extend(crates[-1::-1])

print("".join([stack[-1].replace("[","").replace("]","") for stack in stacks]))



