from get_input import *

url = "https://adventofcode.com/2022/day/1/input"
biggest = 0

text = str(get_input(url))[2:-4]
elf_list = text.split('\\n\\n')
sum_list = []

for i in range(0, len(elf_list)):
    elf_list[i] = elf_list[i].split('\\n')
    elf_list[i] = [int(j) for j in elf_list[i]]
    sum_list.append((i, sum(elf_list[i])))

sum_list.sort(key=lambda y: y[1])
print(sum_list[-3:])
print(sum(n for _, n in sum_list[-3:]))
