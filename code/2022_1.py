f = open("input_2022_1.txt")
input = f.readlines()

res = 0
temp = 0

for i in range(len(input)):
    if input[i] == "\n":
        temp = 0
    else:
        temp += int(input[i])

    if temp > res:
        res = temp

print(res)
