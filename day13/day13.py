from fileinput import input
"""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
lines = [eval(line.strip()) for line in input() if line.strip() != ""]

#
# ---------- PART 1 ------------
#
WRONG = -1
NEUTRAL = 0
RIGHT = 1
def check_order(left, right):
    #1. If both are ints
    if isinstance(left, int) and isinstance(right, int):
        if right < left:
            return WRONG # Wrong order
        elif right == left:
            return NEUTRAL  # Identical, continue checking
        else:
            return RIGHT  # Right order
 
    # 2. If mixed types, make both list
    if isinstance(left, int) and not isinstance(right, int):
        left = [left] 
    if not isinstance(left, int) and isinstance(right, int):
        right = [right]

    # 3. Both are lists
    for i in range(len(left)):
        if len(right) == i: # Right ran out of items, wrong order
            return WRONG
        
        order = check_order(left[i], right[i])
        if order == WRONG or order == RIGHT:
            return order


    return True



pairs = []
for i, (left, right) in enumerate(zip(lines[::2], lines[1::2])):
    order = check_order(left, right)
    if order == RIGHT:
        pairs.append(i+1)

print(sum(pairs))
