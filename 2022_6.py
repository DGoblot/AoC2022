f = open("input_2022_6.txt")
input = f.readlines()
input = input[0].strip()

for i in range(0, len(input)-13):
    temp = 1
    msg = input[i:i+14]
    for j in range(1,14):
        if msg.count(msg[j]) > 1:
            temp = 0
            break
    if temp == 1:
        print(i+14)
        break
            

f.close()
