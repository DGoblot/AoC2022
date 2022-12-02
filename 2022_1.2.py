f = open("input_2022_1.txt")
input = f.readlines()

res = 0
res_tot = 0
temp = 0
ligne_tmp = []
ligne_res = []

for j in range(3):
    res = 0
    temp = 0
    ligne_tmp = []
    ligne_res = []
    for i in range(len(input)):
        if input[i] == "\n":
            temp = 0
            ligne_tmp = []
        else:
            temp += int(input[i])
            ligne_tmp.append(i)

        if temp > res:
            res = temp
            ligne_res = ligne_tmp
            
    del input[ligne_res[0]:ligne_res[-1]+1]
        
    res_tot += res

print(res_tot)

f.close()
