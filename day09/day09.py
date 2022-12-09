import fileinput

"""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
moves = [line.strip().split(" ") for line in fileinput.input()]
moves = [(move[0], int(move[1])) for move in moves]

def move_tail(head, tail):
    # Move tail
    if head[0] == tail[0] and head[1] == tail[1]:
        """
            ***
            *H*  <-- If head and tail in the same position
            ***
        """
        return tail

    elif abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
        """
            *****
            *HHH* 
            *HTH*  <-- If Head is at most 1 abs()-distance away from Tail 
            *HHH*
            *****
        """
        return tail

    else:
        """
            *HHH*                                     *HHH*
            H***H                                     H*T*H
            H*T*H  <-- If Head moved 1 away then -->  HT#TH 
            H***H                                     H*T*H 
            *HHH*                                     *HHH*
        """
        if direction == "R":
            tail = (tail[0]+1, tail[1])
        elif direction == "L":
            tail = (tail[0]-1, tail[1])
        elif direction == "U":
            tail = (tail[0], tail[1]-1)
        elif direction == "D":
            tail = (tail[0], tail[1]+1)

        if head[0] != tail[0] and head[1] != tail[1]:
            """
                *H*H*                                            *H*H*
                H*T*H                                            HT*TH
                *T#T*  <-- If Head has moved diagonally then --> **#** 
                H*T*H                                            HT*TH 
                *H*H*                                            *H*H*
            """
            if direction == "R" or direction == "L":
                """
                    *****                 *****
                    H***H                 HT*TH
                    *T#T*  <-- If then -> **#** 
                    H***H                 HT*TH 
                    *****                 *****
                """
                tail = (tail[0], head[1])
            else: # direction == "U" or direction == "D":
                """
                    *H*H*                 *H*H* 
                    **T**                 *T*T*
                    **#**  <-- If then -> **#** 
                    **T**                 *T*T* 
                    *H*H*                 *H*H* 
                """ 
                tail = (head[0], tail[1])
    return tail

def move_head(head, direction):       
    if direction == "R":
        head = (head[0]+1, head[1])
    elif direction == "L":
        head = (head[0]-1, head[1])
    elif direction == "U":
        head = (head[0], head[1]-1)
    elif direction == "D":
        head = (head[0], head[1]+1)
    
    return head


#
# ----- PART 1 -----
# 
tail = (0,0)
head = (0,0)
visited = { (0,0): True }

for (direction, steps) in moves: 
    for step in range(steps):
        # Move head
        head = move_head(head, direction)
        tail = move_tail(head, tail)
 
        visited[tail] = True
        # Update visited

print(len(visited))

#
# -------- PART 2 -----
#
visited = { (0,0): True }
knots = [(0,0) for i in range(10)]

for (direction, steps) in moves:
    for step in range(steps):
        knots[0] = move_head(knots[0], direction)

        for i, tail in enumerate(knots[1:]):
            knots[i+1] = move_tail(knots[i], tail)
        
        print(knots[-1], direction, knots[0])
        visited[knots[-1]] = True
            

print(visited)
print(len(visited))
