f = open("input_2022_2.txt")
input = f.readlines()

res_tot = 0

for i in range(len(input)):
    res = 0
    lui, moi = input[i].strip().split(" ", 1)
    
    match moi:
        case "X":
            match lui:
                case "A":
                    res = 3
                case "B":
                    res = 1
                case "C":
                    res = 2
                    
        case "Y":
            match lui:
                case "A":
                    res = 4
                case "B":
                    res = 5
                case "C":
                    res = 6

        case "Z":
            match lui:
                case "A":
                    res = 8
                case "B":
                    res = 9
                case "C":
                    res = 7
    res_tot += res
            
print(res_tot)
f.close()
