import fileinput

lines = []

for line in fileinput.input():
    lines.append(line)


# Make list of elves

elvestrings = "".join(lines).split("\n\n")

elves = []
for elf in elvestrings:
    items = [int(item) for item in elf.strip().split("\n")]
    elves.append(sum(items))

"""
1000  - The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
2000   
3000   

4000  - The second Elf is carrying one food item with 4000 Calories.

5000  - The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
6000  

7000  - The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
8000   
9000   

10000 - The fifth Elf is carrying one food item with 10000 Calories.
"""


# Find the Elf carrying the most Calories.

#
# ---------- PART 1 ---------------
#
# How many total Calories is that Elf carrying?
elves.sort()
print(elves[-1])



#
# ---------- PART 2 ---------------
#
three_elves_with_most_calories = elves[-1:-4:-1]
print(sum(three_elves_with_most_calories))
