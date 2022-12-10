import fileinput

"""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
"""
instructions = [instruction for instruction in fileinput.input()]
instructions.reverse()

#
# --------- PART 1 ---------
#
X = 1
addx = 0
running = True
instruction = None
i = 0
signal_sum = 0
crt = [["." for x in range(40)] for y in range(6)] # 240 pixels

while running:
    i += 1
    if instruction is None:
        if len(instructions) == 0:
            running = False
            continue 
        instruction = instructions.pop().strip()
    
    #
    # -------- PART 2 ------------
    # Draw on CRT
    x = (i - 1) % 40
    y = (i - 1) // 40
    if abs(X - x) < 2:
        crt[y][x] = "#"


    if (i - 20) % 40 == 0:
        signal_strength = i * X
        signal_sum += signal_strength
    
    if "addx" in instruction:
        if addx != 0:
            X += addx
            addx = 0
            instruction = None
        else:
            _,V = instruction.split(" ")
            V = int(V)
            addx = V
    elif "noop" in instruction:
        instruction = None
    else:
        print(f"UKNONW INSTRUCTION! PANIC!: {instruction}")
        exit()

    print(f"    i {i:<10} X: {X:<10} addx: {addx:<10} sum: {signal_sum}")

print(signal_sum)

for row in crt:
    print(f"{''.join(row)}")

