from curses.ascii import isupper

input_file = open('aoc22_03.txt')
elf_packing_list = input_file.readlines()

sum_item_priority = 0

for line in elf_packing_list:
    rucksack_contents = str(line)
    compartment_size = int(len(rucksack_contents) / 2)
    first_compartment_contents = set(rucksack_contents[:compartment_size])
    second_compartment_contents = set(rucksack_contents[compartment_size:])
    common_content = str(first_compartment_contents.intersection(second_compartment_contents))
    common_content = common_content[2]
    if isupper(common_content):
        sum_item_priority += ord(common_content)-64+26
    else:
        sum_item_priority += ord(common_content)-96

print(sum_item_priority)

# If you need to get a one-based result instead of the Unicode
# code point of the character, subtract 96 for lowercase characters or 64 for uppercase characters.

input_file.close()
