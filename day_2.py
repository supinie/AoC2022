
from get_input import *


url = "https://adventofcode.com/2022/day/2/input"

text = str(get_input(url))[2:-4]

tournament = text.split('\\n')

score1 = 0
score2 = 0
for round in tournament:
    if round[-1] == "X":
        score1 += 1
        if round[0] == "A":
            score1 += 3
        elif round[0] == "C":
            score1 += 6
    elif round[-1] == "Y":
        score1 += 2
        if round[0] == "A":
            score1 += 6
        elif round[0] == "B":
            score1 += 3
    else:
        score1 += 3
        if round[0] == "B":
            score1 += 6
        elif round[0] == "C":
            score1 += 3


print(score1)

for round in tournament:
    if round[-1] == "X":
        if round[0] == "A":
            score2 += 3
        elif round[0] == "B":
            score2 += 1
        else:
            score2 += 2
    elif round[-1] == "Y":
        score2 += 3
        if round[0] == "A":
            score2 += 1
        elif round[0] == "B":
            score2 += 2
        else:
            score2 += 3
    else:
        score2 += 6
        if round[0] == "A":
            score2 += 2
        elif round[0] == "B":
            score2 += 3
        else:
            score2 += 1

print(score2)

# note to self: read about mappings
