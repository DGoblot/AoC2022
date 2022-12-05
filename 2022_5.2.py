f = open("input_2022_5.txt")
input = f.readlines()

plan = [[] for i in range(9)]
temp = []

for i in range(8):
    for j in range(9):
        if input[i][j*4 + 1] != " ":
            plan[j].append(input[i][j*4 + 1])

for i in range(10, len(input)):
    temp = []
    _, nb, _, start, _, end = input[i].strip().split(" ")
    nb, start, end = int(nb), int(start) - 1, int(end) - 1
    
    temp = plan[start][0:nb]
    temp.extend(plan[end])
    plan[end] = temp
    del plan[start][0:nb]

for i in range(9):
    print(plan[i][0])
