from fileinput import input

"""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
# Read input
_map = [[cell for cell in row.strip()] for row in input()]

# Add padding
hightmap = [["å" for _ in range(len(_map[0])+2)] for _ in range(len(_map)+2)]
for y, row in enumerate(_map):
    for x, cell in enumerate(row):
        hightmap[y+1][x+1] = cell


def find_steps_to_best_signal(start, hightmap):
    # Simulate dijkstra-ish algorithm
    seen = {}
    horizon = {start: 1}
    hightmap[start[1]][start[0]] = "a"
    steps = 0

    while True:
        steps += 1
        new_horizon = {}        
        def check_candidate(cx,cy,x,y):

            if hightmap[y][x] == "z"\
            and hightmap[cy][cx] == "E":
                return True # Found the top with the best signal !!
            
            if (cx,cy) in seen:
                return False 

            if (cx,cy) in new_horizon:
                return False

            if ord(hightmap[cy][cx]) - ord(hightmap[y][x]) <= 1:
                new_horizon[(cx,cy)] = 1
            
            return False

        if len(horizon) == 0:
            return -1

        for x,y in horizon:
            found = check_candidate(x-1,y,x,y)
            if found: break
      
            found = check_candidate(x+1,y,x,y)
            if found: break
                    
            found = check_candidate(x,y-1,x,y)
            if found: break
            
            found = check_candidate(x,y+1,x,y)
            if found: break

            seen[(x,y)] = 1
        
        if found: break
        
        horizon = new_horizon

    return steps

#
# ---------- PART 1 ----------
#
start = (0,0)
# Find start position
for y, row in enumerate(hightmap):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x,y)
            break
    if cell == "S":
        break

steps = find_steps_to_best_signal(start, hightmap)
print(steps)

#
# ------------- PART 2 ------------
#
start_positions = []
for y, row in enumerate(hightmap):
    for x, cell in enumerate(row):
        if cell == "a":
            start_positions.append((x,y))


results = []
for start in start_positions:
    steps = find_steps_to_best_signal(start, hightmap)
    results.append(steps)
    
results = list(filter(lambda a: a != -1, results))

results.sort()
print(results[0])


