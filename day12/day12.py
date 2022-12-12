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
horizon = [(1,1)]
map[1][1] = "a"
steps = 0

while running:
    steps += 1
    new_horizon = []
    def check_candidate(cx,cy,x,y):
        global steps 

        if steps > 251:
            print(steps, map[cy][cx])

        if map[y][x] == "z"\
        and map[cy][cx] == "E":
            global running
            running = False # end loop!!

        elif (cx,cy) not in seen\
        and (cx,cy) not in new_horizon\
        and abs(ord(map[cy][cx]) - ord(map[y][x])) <= 1:
            new_horizon.append((cx,cy))

    for x,y in horizon:
        check_candidate(x-1,y,x,y)
        check_candidate(x+1,y,x,y)
        check_candidate(x,y-1,x,y)
        check_candidate(x,y+1,x,y)

        seen.append((x,y))
    
    horizon = new_horizon


print(steps)