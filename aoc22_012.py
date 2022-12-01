input_file = open('aoc22_01.txt')
elf_calories = input_file.readlines()

import array

max_calories = 0
top_three_elf_calories = [0,0,0]
current_elf_calories: int = 0

for line in elf_calories:
    if line.strip() == '':
        if current_elf_calories > top_three_elf_calories[2]:
            if current_elf_calories > top_three_elf_calories[1]:
                if current_elf_calories > top_three_elf_calories[0]:
                    top_three_elf_calories[2]=top_three_elf_calories[1]
                    top_three_elf_calories[1]=top_three_elf_calories[0]
                    top_three_elf_calories[0]=current_elf_calories
                else:
                    top_three_elf_calories[2]=top_three_elf_calories[1]
                    top_three_elf_calories[1]=current_elf_calories
            else:
                top_three_elf_calories[2]=current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories = 0
    else:
        try:
            calories_on_line = float(line)
            current_elf_calories += calories_on_line
        except:
            pass

max_calories = sum(top_three_elf_calories)
print(max_calories)

input_file.close()
