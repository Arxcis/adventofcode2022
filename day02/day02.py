
import fileinput

# A Y
# B X
# C Z
rounds = []
for line in fileinput.input():
   if line.strip() != "":
        opponent, me = line.strip().split(" ")
        rounds.append((opponent, me))

#
# --------------- PART 1 ------------------
#

#The score for a single round is the score for the shape you selected 
# (1 for Rock, 
#  2 for Paper, and 
#  3 for Scissors) 
#
# plus the score for the outcome of the round (
#  0 if you lost, 
#  3 if the round was a draw, and 
#  6 if you won).
Rock = 1
Paper = 2
Scissors = 3
Loose = 0
Draw = 3
Win = 6

score_rules = {
    # If opponent selects Rock - "A"
    ("A","X"): Rock + Draw,     # then Rock draws with score 1 + 3 = 4
    ("A","Y"): Paper + Win,     # then Paper wins with score 2 + 6 = 8
    ("A","Z"): Scissors + Loose,# then Scissors loose with score 3 + 0 = 3 

    # If opponent selects Paper - "B"
    ("B","X"): Rock + Loose,
    ("B","Y"): Paper + Draw,
    ("B","Z"): Scissors + Win,

    # If opponent selects Scissors - "C"
    ("C","X"): Rock + Win,
    ("C","Y"): Paper + Loose,
    ("C","Z"): Scissors + Draw 
}

total_score = 0

for opponents_choice, my_choice in rounds:
    my_score = score_rules[(opponents_choice, my_choice)]
    total_score += my_score

print(total_score)

#
# ------------------- PART 2 -------------------
#

# "X" - You need to loose
# "Y" - You need to draw
# "Z" - You need to win
ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"

trickery_rules = {
    # If opponent selects Rock - "A"
    ("A","X"): SCISSORS,  # then I choose scissors to loose
    ("A","Y"): ROCK,      # then I choose rock to draw
    ("A","Z"): PAPER,     # then I choose paper to win  

    # If opponent selects Paper - "B"
    ("B","X"): ROCK,
    ("B","Y"): PAPER,
    ("B","Z"): SCISSORS,

    # If opponent selects Scissors - "C"
    ("C","X"): PAPER,
    ("C","Y"): SCISSORS,
    ("C","Z"): ROCK 
}

total_score = 0
for opponents_choice, my_trickery in rounds:
    my_choice = trickery_rules[(opponents_choice, my_trickery)]
    my_score = score_rules[(opponents_choice, my_choice)]
    total_score += my_score

print(total_score)

