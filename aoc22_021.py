"""
First column: A for Rock, B for Paper, and C for Scissors.
Second column: X for Rock, Y for Paper, and Z for Scissors.
Round Outcome Score: win = 6pts, draw = 3pts, loss = 0
Selected Shape Score: 1 for Rock (X), 2 for Paper (Y), and 3 for Scissors(Z)
"""

# Victory for me: 'A Y', 'B Z', 'C X'
# Draw: 'A X', 'B Y, 'C Z'

input_file = open('aoc22_02.txt')
elf_strategy_guide = input_file.readlines()

my_total_round_score = 0
my_total_shape_score = 0

for line in elf_strategy_guide:
    suggested_strategy = str(line)
    # Victory for me: 'A Y', 'B Z', 'C X'
    # Draw: 'A X', 'B Y, 'C Z'
    if suggested_strategy[0:3] == 'A Y' or suggested_strategy[0:3] == 'B Z' or suggested_strategy[0:3] == 'C X':
        my_total_round_score += 6
    elif suggested_strategy[0:3] == 'A X' or suggested_strategy[0:3] == 'B Y' or suggested_strategy[0:3] == 'C Z':
        my_total_round_score += 3
    else:
        pass
    if suggested_strategy[2] == 'X':
        my_total_shape_score += 1
    elif suggested_strategy[2] == 'Y':
        my_total_shape_score += 2
    elif suggested_strategy[2] == 'Z':
        my_total_shape_score += 3
    else:
        pass

print(my_total_round_score)
print(my_total_shape_score)
print(my_total_shape_score + my_total_round_score)

input_file.close()
