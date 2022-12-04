# Day 1 Part 1

# Functions
def read_file(filename):
    file = open(filename, "r")
    lines =[]
    for line in file:
        line = line.strip()
        lines.append(line)
    return lines


def obtain_calories(lines):
    calories = 0
    master_list = []
    i = 0
    while i < len(lines):
        if lines[i] == "":
            master_list.append(calories)
            calories = 0
        else:
            calories = calories + int(lines[i])
        i += 1
    master_list.sort()
    return master_list
        
# Main Code for Part 1
file_information = read_file("input.txt")
calories_elfs = obtain_calories(file_information)
print("Solution Part 1: ", calories_elfs[-1])

# Day 1 - Part 2

# Main Code for Part 2
top_elfs = calories_elfs[-1] + calories_elfs[-2] + calories_elfs[-3]
print("Solution Part 2: ", top_elfs)
