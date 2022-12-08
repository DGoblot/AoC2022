f = open("input_2022_8.txt")
input = f.readlines()

tab = []
maxl = len(input) - 1
maxc = len(input[0].strip()) - 1

for i in range(len(input)):
    for j in range(len(input[i].strip())):
        a = int(input[i][j])

        vis1, vis2, vis3, vis4 = 0, 0, 0, 0
        
        if i != 0 and j != 0 and i != maxl and j != maxc:  

            if i > 1:
                vis1 = i 
                for k in range(i-1, 0, -1):
                    if int(input[k][j]) >= a:
                        vis1 = i - k
                        break
            else:
                vis1 = 1

            if i < maxl - 1:
                vis2 = maxl - i
                for k in range(i+1,len(input)):
                    if int(input[k][j]) >= a:
                        vis2 = k - i
                        break
            else:
                vis2 = 1

            if j > 1:
                vis3 = j
                for k in range(j-1, 0, -1):
                    if int(input[i][k]) >= a:
                        vis3 = j - k
                        break
            else:
                vis3 = 1

            if j < maxc - 1:
                vis4 = maxc - j
                for k in range(j+1,len(input[0].strip())):
                    if int(input[i][k]) >= a:
                        vis4 = k - j
                        break
            else:
                vis4 = 1

        tab.append(vis1*vis2*vis3*vis4)


res = max(tab)
print(res)    

f.close()


    
