# Day 2 PART 1

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

ROCK_YOU = "X"
PAPER_YOU = "Y"
SCISSORS_YOU = "Z"

SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSORS = 3

DRAW = 3
WIN = 6
def readfile(file_name):
    file = open(file_name, "r")
    file_information = []
    for line in file:
        line = line.strip().split()
        file_information.append(line)
    file.close()
    return file_information

def process_info(file_info):
    score = 0
    for line in file_info:
        if line[0] == ROCK and line[1] == PAPER_YOU:
            score = score + SCORE_PAPER + WIN
        elif line[0] == ROCK and line[1] == ROCK_YOU:
            score = score + SCORE_ROCK + DRAW
        elif line[0] == ROCK and line[1] == SCISSORS_YOU:
            score = score + SCORE_SCISSORS
            
        elif line[0] == PAPER and line[1] == PAPER_YOU:
            score = score + SCORE_PAPER + DRAW
        elif line[0] == PAPER and line[1] == ROCK_YOU:
            score = score + SCORE_ROCK
        elif line[0] == PAPER and line[1] == SCISSORS_YOU:
            score = score + SCORE_SCISSORS + WIN

        elif line[0] == SCISSORS and line[1] == PAPER_YOU:
            score = score + SCORE_PAPER
        elif line[0] == SCISSORS and line[1] == ROCK_YOU:
            score = score + SCORE_ROCK + WIN
        elif line[0] == SCISSORS and line[1] == SCISSORS_YOU:
            score = score + SCORE_SCISSORS + DRAW
    return score
            
file_info = readfile("input.txt")
total_score = process_info(file_info)
print("First Solution:", total_score)

# DAY 2 PART 2

'''
PAPER_YOU = Y = DRAW
ROCK_YOU = X = LOSE
SCISSORS_YOU = Z = WIN
'''
def process_info2(file_info):
    score = 0
    for line in file_info:
        if line[0] == ROCK and line[1] == PAPER_YOU:
            score = score + SCORE_ROCK + DRAW
        elif line[0] == ROCK and line[1] == ROCK_YOU:
            score = score + SCORE_SCISSORS
        elif line[0] == ROCK and line[1] == SCISSORS_YOU:
            score = score + SCORE_PAPER + WIN
            
        elif line[0] == PAPER and line[1] == PAPER_YOU:
            score = score + SCORE_PAPER + DRAW
        elif line[0] == PAPER and line[1] == ROCK_YOU:
            score = score + SCORE_ROCK
        elif line[0] == PAPER and line[1] == SCISSORS_YOU:
            score = score + SCORE_SCISSORS + WIN

        elif line[0] == SCISSORS and line[1] == PAPER_YOU:
            score = score + SCORE_SCISSORS + DRAW
        elif line[0] == SCISSORS and line[1] == ROCK_YOU:
            score = score + SCORE_PAPER
        elif line[0] == SCISSORS and line[1] == SCISSORS_YOU:
            score = score + SCORE_ROCK + WIN
    return score

total_score2 = process_info2(file_info)
print("Second Solution:", total_score2)
