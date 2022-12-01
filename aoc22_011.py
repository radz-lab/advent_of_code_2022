input_file = open('aoc22_01.txt')
elf_calories = input_file.readlines()

max_calories = 0
current_elf_calories = 0

for line in elf_calories:
    if line.strip() == '':
        if current_elf_calories > max_calories:
            max_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories = 0
    else:
        try:
            calories_on_line = float(line)
            current_elf_calories += calories_on_line
        except:
            pass

print(max_calories)

input_file.close()
