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
def count_minutes(target: str, parent: dict, valve: dict, seen: set, count: int):
    if target == valve["name"]:
        return count
    
    counts = []
    for tunnel in valve["tunnels"]:
        if tunnel == parent["name"]:
            continue
        if (valve["name"], tunnel) in seen:
            continue
        counts.append(count_minutes(target, valve, valves[tunnel], set([(valve["name"], tunnel), *seen]), count + 1))

    if len(counts) == 0:
        return 999_999

    return min(counts)


print(valves.values())

for it in valves:
    for ot in valves:
        minutes = count_minutes(ot, valves[it], valves[it], set(), int())
        valves[it]["minutes"][ot] = minutes

        print(it, ot)

#
# Part 1
#
from itertools import permutations
perm = valves.values()
print(f"len(perm): {len(perm)}")

perm = filter(lambda x: x["flow"] != 0, valves.values())
print(f"len(perm): {len(perm)}")

perm = map(lambda x: x["name"], perm)
print(f"len(perm): {len(perm)}")

perm = permutations(perm)
print(f"len(perm): {len(perm)}")

def compute_pressure(keys, valves):
    current = "AA"
    minute = 1
    pressure = 0
    total = 0

    print(keys)
    print(f"\n== MINUTE {minute} ==")
    print(f"Releasing {pressure} pressure")

    for next in keys:
        print(f"At {current}, moving to {next}")
        print(f"Total {total}")

        # Step 1: Move to new node, and open it, taking X minutes
        minute += valves[current]["minutes"][next]
        total += pressure * valves[current]["minutes"][next]
        print(f"\n== MINUTE {minute} ==")
        print(f"Releasing {pressure} pressure")
        print(f"At {next}, opening valve with {valves[next]['flow']} pressure")
        print(f"Total {total}")
        pressure += valves[next]["flow"]

        # Step 2: Wait one minute, increasing pressure, taking 1 minute
        minute += 1
        total += pressure * 1
        print(f"\n== MINUTE {minute} ==")
        print(f"Releasing {pressure} pressure")
    
        # Step 3: Make next the new current
        current = next

    print(f"Total {total}")

    for minute in range(minute+1, 31):
        total += pressure * 1
        print(f"\n== MINUTE {minute} ==")
        print(f"Releasing {pressure} pressure")
        print(f"Total {total}")

max_pressure = 0
pressure = compute_pressure(("DD", "BB", "JJ", "HH", "EE", "CC"), valves)
print(pressure)
exit(0)

for i, keys in enumerate(perm):
    pressure = compute_pressure(keys, valves)
    if pressure > max_pressure:
        max_pressure = pressure

print(f"max_pressure: {max_pressure}")