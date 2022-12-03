import fileinput

#
# ------------ INPUT
#
"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
rucksacks = []
for line in fileinput.input():
    if line.strip() == "":
        continue

    items = line.strip()
    first_compartment = items[0:len(items)//2]
    second_compartment = items[len(items)//2:]

    rucksack = (first_compartment, second_compartment)
    rucksacks.append(rucksack)


#
# ------------- PART 1
#
double_letters = []
for first_compartment,second_compartment in rucksacks:
    seen = {}

    for letter in first_compartment:
        seen[letter] = 1
    for letter in second_compartment:
        if letter in seen:
            double_letters.append(letter)
            break

"""
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
"""
priorities = []
for letter in double_letters:
    # if small letter
    if ord(letter) > ord('a') and ord(letter) <= ord('z'):
        priority = ord(letter) - ord('a') + 1
    elif ord(letter) > ord('A') and ord(letter) <= ord('Z'):
        priority = ord(letter) - ord('A') + 27
    else: #scream
        print(f"UNKNOWN LETTER: {letter}!!!")
        exit()
    
    priorities.append(priority)

print(sum(priorities))

#
# ---------- PART 2
#
group_badges = []
for group_index in range(0,len(rucksacks), 3):

    group_rucksacks = rucksacks[group_index:group_index+3]
    
    seen_group = {}
    for first_compartment,second_compartment in group_rucksacks:
        items = f"{first_compartment}{second_compartment}"

        seen_rucksack = {}
        for item in items:
            if item not in seen_rucksack:
                seen_rucksack[item] = 1

        for seen in seen_rucksack:
            if seen not in seen_group:
                seen_group[seen] = 1
            else:
                seen_group[seen] += 1

    for item, occurance in seen_group.items():
        if occurance == 3: # seen in all 3 rucksacks 
            group_badges.append(item)

priorities = []
for letter in group_badges:
    # if small letter
    if ord(letter) > ord('a') and ord(letter) <= ord('z'):
        priority = ord(letter) - ord('a') + 1
    elif ord(letter) > ord('A') and ord(letter) <= ord('Z'):
        priority = ord(letter) - ord('A') + 27
    else: #scream
        print(f"UNKNOWN LETTER: {letter}!!!")
        exit()
    
    priorities.append(priority)

print(sum(priorities))

   










