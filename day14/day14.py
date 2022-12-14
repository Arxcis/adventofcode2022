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

max_x = max(flat_lines, key=lambda it: it[0])[0] + 120
max_y = max(flat_lines, key=lambda it: it[1])[1] + 1

START = "+"
AIR = "."
SAND = "o"
DUST = "~"
ROCK = "#"

sand_start = (500,0)
grid = [[AIR for x in range(max_x)] for y in range(max_y)]
grid[sand_start[1]][sand_start[0]] = START


def print_grid(grid):
    for line in grid:
        print("".join(line[400:]))


def make_grid():
    grid = [[AIR for x in range(max_x)] for y in range(max_y)]
    grid[sand_start[1]][sand_start[0]] = START

    for rock_line in rocks:
        for a,b in zip(rock_line[0:-1], rock_line[1:]):
            if a[1] == b[1]:
                y = a[1]
                if a[0] < b[0]:
                    for x in range(a[0], b[0]+1):
                        grid[y][x] = ROCK
                else:
                    for x in range(a[0], b[0]-1, -1):
                        grid[y][x] = ROCK

            elif a[0] == b[0]: 
                x = a[0]
                if a[1] < b[1]:
                    for y in range(a[1], b[1]+1):
                        grid[y][x] = ROCK 
                else:
                    for y in range(a[1], b[1]-1, -1):
                        grid[y][x] = ROCK
            else:
                print(a,b)
                print("PANIC!!")
                exit()
    return grid

def simulate_sand(grid):
    i = 0

    # Simulate sand
    while True:
        x,y = sand_start 
        
        # Simulate grain
        while True:
            # If below is air, sand falls 
            if grid[y+1][x] == AIR or grid[y+1][x] == DUST:
                y += 1
                grid[y][x] = DUST
            # else check down+left
            elif grid[y+1][x-1] == AIR or grid[y+1][x-1] == DUST: 
                y += 1
                x -= 1
                grid[y][x] = DUST
            # else check down+right
            elif grid[y+1][x+1] == AIR or grid[y+1][x+1] == DUST: 
                y += 1
                x += 1
                grid[y][x] = DUST
            # else sand is at rest :)
            else:
                i += 1
                grid[y][x] = SAND
                break
        


            # If sand is falling into the abyss...
            if y == len(grid)-1: break
        if y == len(grid)-1: break
        
        # If sand is blocking sand_start
        if y == sand_start[1] and x == sand_start[0]: break
    
    return i

#
# -------------- PART 1 -------------
#
grid = make_grid()
i = simulate_sand(grid)
print(i)

#
# -------------- PART 2 -------------
#
grid = make_grid()
grid.append([AIR for i in range(len(grid[0]))])
grid.append([ROCK for i in range(len(grid[0]))])

i = simulate_sand(grid)
print_grid(grid)
print(i)
