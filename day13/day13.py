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
CONTINUE = 0
RIGHT = 1
def check_order(left, right):
    #1. If both are ints
    print(f"- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("- Left side is smaller, so inputs are in the right order")
            return RIGHT    # Right order
        elif right == left:
            return CONTINUE  # Identical, continue checking
        else:
            print(f"- Right side is smaller, so inputs are not in the right order")
            return WRONG    # Wrong order
 
    # 2. If mixed types, make both list
    if isinstance(left, int) and not isinstance(right, int):
        print(f"- mixed types; convert left to [{left}] and retry comparison")
        left = [left] 
    if not isinstance(left, int) and isinstance(right, int):
        print(f"- mixed types; convert right to [{right}] and retry comparison")
        right = [right]

    # 3. Both are lists
    for i in range(len(left)):
        if len(right) == i: # Right ran out of items, wrong order
            print(f"- Right side ran out of items, so inputs are not in the right order")
            return WRONG
        
        order = check_order(left[i], right[i])
        if order == WRONG or order == RIGHT:
            return order

    if len(left) < len(right):
        print(" - Left side ran out of items, so inputs are in the right order")
        return RIGHT

    return CONTINUE



pairs = []
for i, (left, right) in enumerate(zip(lines[::2], lines[1::2])):
    print(f"\n==== PAIR {i+1} ====")
    order = check_order(left, right)
    if order == RIGHT or order == CONTINUE:
        pairs.append(i+1)
    
print(pairs)
print(sum(pairs))

#
# ------- PART 2 ---------
#
pairs = [(left, right) for left, right in zip(lines[::2], lines[1::2])]
from functools import cmp_to_key, reduce

lines.append([[2]])
lines.append([[6]])
sorted_lines = sorted(lines, key=cmp_to_key(lambda left,right: check_order(left, right)), reverse=True)

decoder_indicies = []
for i, l in enumerate(sorted_lines):
    print(l)
    if isinstance(l, list) and len(l) == 1:
        if isinstance(l[0], list) and len(l[0]) == 1:
            if l[0][0] == 2 or l[0][0] == 6:
                decoder_indicies.append(i+1)

decoder_key = reduce(lambda a,b: a*b, decoder_indicies)

print(decoder_key)


