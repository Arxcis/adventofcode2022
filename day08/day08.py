import fileinput

"""
30373
25512
65332
33549
35390
"""
grid = [[int(tree) for tree in row.strip()] for row in fileinput.input()]

omkrets = (len(grid) - 1) * 4

#
# ---------- PART 1 ---------------
#
trees_visible = []
for y, row in enumerate(grid[1:-1]):
    y = y + 1
    for x, tree in enumerate(row[1:-1]):
        x = x + 1

        up = []
        for row in grid[y-1::-1]:
            if row[x] >= tree: break
            up.append(row[x])
            
        down = []
        for row in grid[y+1::]:
            if row[x] >= tree: break
            down.append(row[x])
            
        left = []
        for left_tree in grid[y][x-1::-1]:
            if left_tree >= tree: break
            left.append(left_tree)

        right = []
        for right_tree in grid[y][x+1::]:
            if right_tree >= tree: break
            right.append(right_tree)

        if len(up) - y == 0\
            or len(down) + y == len(grid) - 1\
            or len(left) - x == 0\
            or len(right) + x == len(grid) - 1:
            trees_visible.append((x,y,tree))
        else:
            pass

print(len(trees_visible) + omkrets)


#
# ---------- PART 2 ---------------
#
best_scenic_score = 0
for y, row in enumerate(grid[1:-1]):
    y = y + 1
    for x, tree in enumerate(row[1:-1]):
        x = x + 1

        up = []
        for row in grid[y-1::-1]:
            up_tree = row[x]
            up.append(up_tree)
            if up_tree >= tree: break

        down = []
        for row in grid[y+1::]:
            down_tree = row[x]
            down.append(down_tree)
            if down_tree >= tree: break

        left = []
        for left_tree in grid[y][x-1::-1]:
            left.append(left_tree)
            if left_tree >= tree: break

        right = []
        for right_tree in grid[y][x+1::]:
            right.append(right_tree)
            if right_tree >= tree: break


        scenic_score = len(up) * len(down) * len(right) * len(left)
        if best_scenic_score < scenic_score:
            best_scenic_score = scenic_score

print(best_scenic_score)