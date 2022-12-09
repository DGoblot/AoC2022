f = open("input_2022_9.txt")
input = f.readlines()

res = 0
tab_res = []
hx = 0
hy = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
x4 = 0
y4 = 0
x5 = 0
y5 = 0
x6 = 0
y6 = 0
x7 = 0
y7 = 0
x8 = 0
y8 = 0
x9 = 0
y9 = 0

def next_knot(hx,hy,tx,ty):
    if hx > tx + 1:
        tx += 1
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
            
    elif hx < tx - 1:
        tx -= 1
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
            
    elif hy > ty + 1:
        ty += 1
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
            
    elif hy < ty - 1:
        ty -= 1
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
                    
    return tx,ty

for i in range(len(input)):
    direc, nb = input[i].strip().split(" ")
    for i in range(int(nb)):

        match direc:
            case "R": 
                hx += 1
            case "D": 
                hy -= 1
            case "L": 
                hx -= 1
            case "U": 
                hy += 1
                
        x1, y1 = next_knot(hx, hy, x1, y1)
        x2, y2 = next_knot(x1, y1, x2, y2)
        x3, y3 = next_knot(x2, y2, x3, y3)
        x4, y4 = next_knot(x3, y3, x4, y4)
        x5, y5 = next_knot(x4, y4, x5, y5)
        x6, y6 = next_knot(x5, y5, x6, y6)
        x7, y7 = next_knot(x6, y6, x7, y7)
        x8, y8 = next_knot(x7, y7, x8, y8)
        x9, y9 = next_knot(x8, y8, x9, y9)
        
        tab_res.append((x9,y9))

res = len(set(tab_res))
print(res)

f.close()


    
    
