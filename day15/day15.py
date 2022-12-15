from fileinput import input
from re import findall
"""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
sensors = [[(int(sx),int(sy),int(bx),int(by)) for sx,sy,bx,by in findall(
    "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line
)][0] for line in input()]

def find_impossible_positions(y: int, beacons_on_y: set, impossible_positions_on_y: set):
    for sensor in sensors:
        sx,sy,bx,by = sensor
        """
        ....B<-----|#######.... sb_distance
        ...########|########...
        ..#########S#########.. 
        ...#################...
        ....###############....
        """
        sb_distance = abs(bx-sx) + abs(by-sy)
        """
        ....B######^########.... sy_distance
        ...########|########...
        ..#########S#########.. 
        ...#################...
        ....###############....
        """
        sy_distance = abs(y-sy)

        """
        ....B##############....
        ...#################...
        ..#########S#########.. [<- max_y ->]
        ...#################...
        ....###############....
        """
        max_y = (sb_distance * 2) + 1

        """
        ....B##############.... [<- y_coverage ->]
        ...#################...
        ..#########S#########.. 
        ...#################...
        ....###############....
        """
        y_coverage = max_y - (sy_distance*2)
        if y_coverage > 0:
            impossible_positions_on_y.add((sx,y))
            for i in range(1, (y_coverage // 2)+1):
                impossible_positions_on_y.add((sx+i,y))
                impossible_positions_on_y.add((sx-i,y))

        if by == y:
            beacons_on_y.add((bx,by))


#
# ------ Part 1 -------
#
small_input_y = 10
big_input_y = 2_000_000

print("# ------ Part 1 -------")
impossible_positions_on_y = set()
beacons_on_y = set()
find_impossible_positions(big_input_y, beacons_on_y, impossible_positions_on_y)

print(f"len(impossible_positions_on_y): {len(impossible_positions_on_y)}")
print(f"len(beacons_on_y): {len(beacons_on_y)}")
print(len(impossible_positions_on_y) - len(beacons_on_y))

#
# ------ Part 2 -------
#
small_input_range = range(10,21)
big_input_range = range(0, 4_000_000)

print("# ------ Part 2 -------")
impossible_positions_on_y = set()
beacons_on_y = set()
for y in small_input_range:
    find_impossible_positions(y, beacons_on_y, impossible_positions_on_y)
print(len(impossible_positions_on_y) - len(beacons_on_y))


print("Converting set() to list[]...")
positions = [it for it in impossible_positions_on_y]

def cmp(a,b):
    if b[1] == a[1]: 
        return a[0] - b[0]
    return a[1] - b[1]

print("Sorting_positions....")
from functools import cmp_to_key
positions.sort(key=cmp_to_key(cmp))

print("Looking for distress beacon....")
for a,b in zip(positions[0:-1], positions[1:]):
    diff_x = abs(b[0] - a[0])
    diff_y = abs(b[1] - a[1])
    if diff_x > 1 and diff_y == 0:
        print(f"Found distress beacon at: {(a[0]+1, a[1])} !!!")
        exit()
""" 
grid = [["." for x in range(21)] for y in range(10,21)]
for x,y in impossible_positions_on_y:
    if x > 20 or x < 0 or y > 20 or y < 10: continue
    grid[y-10][x] = "#"

for y,row in enumerate(grid):
    str = f"y: {y+10} - {''.join(row)}"
    for x,cell in enumerate(row):
        if cell == ".":
            str += f" <- FOUND distress beacon at: {(x,y+10)} !!"
            
    print(str)
 """