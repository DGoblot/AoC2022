f = open("input_2022_3.txt")
input = f.readlines()

res = 0
test = 0
i = 0

while i < len(input):
    found = 0
    ligne1 = input[i]
    ligne2 = input[i+1]
    ligne3 = input[i+2]
    for j in range(len(ligne1)):
        if found == 0:
            for k in range(len(ligne2)):
                if ligne1[j] == ligne2[k] and found == 0:
                    for t in range(len(ligne3)):
                        if ligne2[k] == ligne3[t]:
                            if ligne1[j].isupper():
                                res += ord(ligne1[j]) - 38
                            else:
                                res += ord(ligne1[j]) - 96
                            found = 1
                            break
    i += 3
                
print(res)          
        
