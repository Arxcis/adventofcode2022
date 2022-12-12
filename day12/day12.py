from fileinput import input

"""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
_map = [[cell for cell in row.strip()] for row in input()]
# Add padding
map = [["å" for _ in range(len(_map[0])+2)] for _ in range(len(_map)+2)]
for y, row in enumerate(_map):
    for x, cell in enumerate(row):
        map[y+1][x+1] = cell

cost_map = [[-1 for _ in range(len(_map[0])+2)] for _ in range(len(_map)+2)]


#
# ---------- PART 1 ----------
running = True
seen = []
cost_map[1,1] = 0
horizon = [(1,1)]

while running:

    left_cost = map[y][x-1] - map[y][x-1]
    right_cost = map[y][x+1]
    up_cost = map[y-1][x]
    down_cost = map[y+1][x]


    