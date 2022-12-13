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
def check_order(left, right):
    # 1. If mixed types, make both int 
    if isinstance(left, int) and not isinstance(right, int):
        while isinstance(right, list):
            if len(right) == 0: return False
            right = right[0]

    if not isinstance(left, int) and isinstance(right, int):
        while isinstance(left, list):
            if len(left) == 0: return True
            left = left[0]
         
    #2. If both are ints
    if isinstance(left, int) and isinstance(right, int):
        if right < left:
            return False
        else:
            return True

    # 3. Both are lists
    if len(right) < len(left):
        return False
    
    for l,r in zip(left, right):
        ordered = check_order(l,r)
        if not ordered:
            return False

    return True



pairs = []
for i, (left, right) in enumerate(zip(lines[::2], lines[1::2])):
    ordered = check_order(left, right)
    if ordered:
        pairs.append(i+1)

print(sum(pairs))
