import fileinput

#
# ------- PARSE -------
#
"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
section_pairs = []
for line in fileinput.input():
    if line.strip() == "": continue

    first_elf, second_elf = line.strip().split(",")
    
    a,b = first_elf.split("-")
    c,d = second_elf.split("-")

    section_pairs.append(((int(a),int(b)),(int(c),int(d))))

#
# ------- PART 1 -------
#
"""
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8   <---- This section fully contains the one below
..34567..  3-7    

.....6...  6-6
...456...  4-6   <---- This section fully contains the one above

.23456...  2-6
...45678.  4-8
"""
fully_contained_pairs = []
for (a,b), (c,d) in section_pairs:
    if c <= a and a <= d and c <= b and b <= d:
        # then (a,b) is fully contained within (c,d)
        fully_contained_pairs.append((a,b))
    elif a <= c and c <= b and a <= d and d <= b:
        # then (c,d) is fully contained within (a,b)
        fully_contained_pairs.append((c,d))

print(len(fully_contained_pairs))


#
# ------- PART 1 -------
#
partially_overlapped_pairs = []
for (a,b), (c,d) in section_pairs:
    if c <= a and a <= d or c <= b and b <= d:
        # then (a,b) is fully contained within (c,d)
        partially_overlapped_pairs.append((a,b))
    elif a <= c and c <= b or a <= d and d <= b:
        # then (c,d) is fully contained within (a,b)
        partially_overlapped_pairs.append((c,d))


print(len(partially_overlapped_pairs))

