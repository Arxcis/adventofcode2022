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
sensors = [[(int(sx),int(sy),int(bx),int(by), abs(int(bx)-int(sx)) + abs(int(by)-int(sy))) for sx,sy,bx,by in findall(
        "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        line
    )][0] for line in input()]

sensor_range_min = min([sx - abs(bx-sx) - abs(by-sy) for (sx,sy,bx,by,_) in sensors])
sensor_range_max = max([sx + abs(bx-sx) + abs(by-sy) for (sx,sy,bx,by,_) in sensors])
def find_intersections(y, sensors):
    intersecting_sensors = []
    intersecting_beacons = set()

    for sx,sy,bx,by,sb_distance in sensors:
        sy_distance = abs(y - sy)

        # If y does not intersect with sensor area
        #   y -------------------  = 10
        #   ...................... = 11
        #   ...........#.......... = 12
        #   ..........B##......... = 13
        #   .........##S##........ = 14
        if sy_distance > sb_distance:
            continue

        # If y intersects with sensor area
        #   ...................... = 07
        #   ...................... = 08
        #   ...........#.......... = 09
        #   y ------- B## -------  = 10
        #   .........##S##........ = 11
        #   ..........###......... = 12
        #   ...........#.......... = 13

        # If Beacon intersects with y
        if by == y:
            intersecting_beacons.add((bx,by))

        #   ...................... = 07
        #   ...........#.......... = 08
        #   y --------B##--------  = 09
        #   .........#####........ = 10
        #   sx_min  X##S##X sx_max = 11
        #   .........#####........ = 12
        #   ..........###......... = 13
        #   ...........#.......... = 14
        #   ...................... = 15
        sx_min = sx - sb_distance
        sx_max = sx + sb_distance + 1

        #   ...................... = 07
        #   ...........#.......... = 08
        #    yx_min   X#X  yx_max  = 09
        #   .........#####........ = 10
        #    sx_min X##S##X sx_max = 11
        #   .........#####........ = 12
        #   ..........###......... = 13
        #   ...........#.......... = 14
        #   ...................... = 15
        yx_min = sx_min + sy_distance
        yx_max = sx_max - sy_distance

        intersecting_sensors.append((yx_min, yx_max))

    return (intersecting_sensors, intersecting_beacons)


#
# ---- Part 1 ----
#
intersecting_lines, intersecting_beacons = find_intersections(10, sensors)
start = min(intersecting_lines, key=lambda line: line[0])[0]
end = max(intersecting_lines, key=lambda line: line[1])[1]
print("Part 1: ", end - start - len(intersecting_beacons))


#
# ---- Part 2 ----
#
for y in range(0, 4_000_000):
    intersecting_lines, intersecting_beacons = find_intersections(y, sensors)
    intersecting_lines.sort()

    for i in range(0,len(intersecting_lines)-1):
        # Check if there is a gap
        a_start,a_end = intersecting_lines[i]
        b_start,b_end = intersecting_lines[i+1]

        if a_end > b_end:
            intersecting_lines[i+1] = (b_start, a_end)
            continue

        if b_start > a_end:
            # FOUND GAP!
            x = a_end
            y = y
            # 11_756_174_628_223
            print(f"a_end: {a_end}, b_start: {b_start}, x: {x}, y: {y}, tuning frequency: {x * 4_000_000 + y}")
            exit(0)
