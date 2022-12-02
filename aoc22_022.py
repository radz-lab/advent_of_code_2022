"""
First column: A for Rock, B for Paper, and C for Scissors.
Second column: X for Lose, Y for Draw, and Z for Win.
Round Outcome Score: win = 6pts, draw = 3pts, loss = 0
Selected Shape Score: 1 for Rock, 2 for Paper, and 3 for Scissors
"""

input_file = open('aoc22_02.txt')
elf_strategy_guide = input_file.readlines()

my_total_round_score = 0
my_total_shape_score = 0

for line in elf_strategy_guide:
    suggested_strategy = str(line)
    print(suggested_strategy[2])
    if suggested_strategy[2] == 'Z':
        my_total_round_score += 6
        if suggested_strategy[0] == 'A':
            my_total_shape_score += 2
        elif suggested_strategy[0] == 'B':
            my_total_shape_score += 3
        else:
            my_total_shape_score += 1
    elif suggested_strategy[2] == 'Y':
        my_total_round_score += 3
        if suggested_strategy[0] == 'A':
            my_total_shape_score += 1
        elif suggested_strategy[0] == 'B':
            my_total_shape_score += 2
        else:
            my_total_shape_score += 3
    elif suggested_strategy[2] == 'X':
        if suggested_strategy[0] == 'A':
            my_total_shape_score += 3
        elif suggested_strategy[0] == 'B':
            my_total_shape_score += 1
        else:
            my_total_shape_score += 2
    else:
        pass

print(my_total_round_score)
print(my_total_shape_score)
print(my_total_shape_score + my_total_round_score)

input_file.close()
