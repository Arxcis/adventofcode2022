from fileinput import input
from re import findall

#
# Parse input
#
"""
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
_valves = [[(
    name,
    int(flow),
    tunnels.replace(" ", "").split(",")
) for name,flow,tunnels in findall(
    "Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)",
    line
)][0] for line in input()]

valves = {}
for name, flow, tunnels in _valves:
    valves[name] = { "name": name, "flow": flow, "tunnels": tunnels, "minutes": {} }

#
# Precompute how far everything is from everything else
#
def count_minutes(target: str, valve: dict, seen: set, count: int):
    if target == valve["name"]:
        return count
    
    if valve["name"] in seen:
        return 999_999
    seen.add(valve["name"])

    counts = []
    for tunnel in valve["tunnels"]:
        counts.append(count_minutes(target, valves[tunnel], seen, count + 1))

    return min(counts)

for it in valves:
    for ot in valves:
        minutes = count_minutes(ot, valves[it], set(), int())
        valves[it]["minutes"][ot] = minutes

#
# Part 1
#
from itertools import permutations
perm = filter(lambda x: x["flow"] != 0, valves.values())
perm = map(lambda x: x["name"], perm)
perm = permutations(perm)

max_pressure = 0

for i, keys in enumerate(perm):
    current = "AA"
    minute = 1
    pressure = 0
    total = 0

    print(keys)
    print(f"\n== MINUTE {minute} ==")
    print(f"Releasing {pressure} pressure")

    for next in keys:
        print(f"At {current}, moving to {next}")

        # Step 1: Move to new node, taking X minutes
        minute += valves[current]["minutes"][next]
        total += pressure * valves[current]["minutes"][next]
        print(f"\n== MINUTE {minute} ==")
        print(f"Releasing {pressure} pressure")
        print(f"At {next}, opening valve with {valves[next]['flow']} pressure")

        # Step 2: Open valve at the new node, increasing pressure, taking 1 minute
        minute += 1
        total += pressure * 1
        pressure += valves[next]["flow"]
        print(f"\n== MINUTE {minute} ==")
        print(f"Releasing {pressure}")
    
        # Step 3: Make next the new current
        current = next

        
    if total > max_pressure:
        max_pressure = total

    break
print(f"max_pressure: {max_pressure}")