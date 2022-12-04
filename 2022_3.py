f = open("input_2022_3.txt")
input = f.readlines()

res = 0
test = 0

for i in range(len(input)):
    found = 0
    ligne = input[i]
    for j in range(int(len(ligne)/2)):
        if found == 0:
            for k in range(int(len(ligne)/2), len(ligne)):
                if ligne[j] == ligne[k]:
                    if ligne[j].isupper():
                        res += ord(ligne[j]) - 38
                    else:
                        res += ord(ligne[j]) - 96
                    found = 1
                    break
                
print(res)          
        
