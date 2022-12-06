import fileinput

input = [line for line in fileinput.input()][0]

#
# ----- PART 1 ------
#
PACKET_HEADER_LEN = 4
for i in range(len(input) - PACKET_HEADER_LEN):
    a,b,c,d = input[i:i+PACKET_HEADER_LEN]

    if a != b and a != c and a != d\
    and b != a and b != c and b != d\
    and c != a and c != b and c != d\
    and d != a and d != b and d != c:
        break

#
# ----- PART 2 ------
#
MESSAGE_HEADER_LEN = 14
for i in range(len(input) - MESSAGE_HEADER_LEN):
    seen = {}
    for char in input[i:i+MESSAGE_HEADER_LEN]:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    
    found = True
    for char,count in seen.items():
        if count > 1:
            found = False
            break
    if found:
        # Found the start of message
        print(i+MESSAGE_HEADER_LEN)
        break

