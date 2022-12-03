from curses.ascii import isupper

input_file = open('aoc22_03.txt')
elf_packing_list = input_file.readlines()

sum_item_priority = 0

for i in range(len(elf_packing_list)):
    if i%3 == 0:
        elf_packing_list
    elif i%3 == 1:
        previous_rucksack = elf_packing_list[i-1]
        this_rucksack = elf_packing_list[i].strip("\n")
        common_content = str(set(this_rucksack).intersection(set(previous_rucksack)))
        print(common_content)
    elif i%3 == 2:
        this_rucksack = elf_packing_list[i]
        common_content = str(set(this_rucksack).intersection(set(common_content)))
        common_content = common_content[2]
        if isupper(common_content):
            sum_item_priority += ord(common_content) - 64 + 26
        else:
            sum_item_priority += ord(common_content) - 96
        print(common_content)

print(sum_item_priority)

input_file.close()
