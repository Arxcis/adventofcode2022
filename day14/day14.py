from fileinput import input
import re
from functools import reduce
"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
"""
rocks = [[(int(x),int(y)) for x,y in re.findall("(\d+),(\d+)", line)] for line in input()]
flat_lines = reduce(lambda a,b: a+b, rocks)

min_x = min(flat_lines, key=lambda it: it[0])[0]
min_y = min(flat_lines, key=lambda it: it[1])[1]

max_x = max(flat_lines, key=lambda it: it[0])[0] + 1
max_y = max(flat_lines, key=lambda it: it[1])[1] + 1

START = "+"
AIR = "."
SAND = "o"
DUST = "~"
ROCK = "#"

sand_start = (500,0)
grid = [[AIR for x in range(max_x)] for y in range(max_y)]
grid[sand_start[1]][sand_start[0]] = START

def print_grid():
    for y in grid:
        print("".join(y[450:]))

for rock_line in rocks:
    for a,b in zip(rock_line[0:-1], rock_line[1:]):
        if a[1] == b[1]:
            y = a[1]
            if a[0] < b[0]:
                for x in range(a[0], b[0]+1):
                    grid[y][x] = ROCK
            if a[0] > b[0]:
                for x in range(a[0], b[0]-1, -1):
                    grid[y][x] = ROCK

        if a[0] == b[0]: 
            x = a[0]
            if a[1] < b[1]:
                for y in range(a[1], b[1]+1):
                    grid[y][x] = ROCK 
            else:
                for y in range(b[1], a[1]-1):
                    grid[y][x] = ROCK 

#
# -------------- PART 1 -------------
#
i = 0 
while True:
    i += 1
    x,y = sand_start 
    
    while True:
        # If one below is air, lower sand
        if grid[y+1][x] == AIR or grid[y+1][x] == DUST:
            y += 1
        # If one below is rock or sand
        else:
            # Check left
            if grid[y+1][x-1] == AIR or grid[y+1][x-1] == DUST: 
                y += 1
                x -= 1
            # check right
            elif grid[y+1][x+1] == AIR or grid[y+1][x+1] == DUST: 
                y += 1
                x += 1
            else:
                break
        
        grid[y][x] = DUST
        if y == len(grid)-1: break
    if y == len(grid)-1: break

    grid[y][x] = SAND
    
    print(f"\n=== {i} === ")
    print_grid()

print(f"\n=== GAME OVER! === ")
print_grid()

print((min_x,min_y), (max_x,max_y))
