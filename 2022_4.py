f = open("input_2022_4.txt")
input = f.readlines()

res = 0

for i in range(len(input)):
    elf1, elf2 = input[i].strip().split(",")
    start1,end1 = elf1.split("-")
    start2,end2 = elf2.split("-")
    if int(start1) <= int(start2) and int(end1) >= int(end2):
        res += 1
    elif int(start1) >= int(start2) and int(end1) <= int(end2):
        res +=1

print(res)
