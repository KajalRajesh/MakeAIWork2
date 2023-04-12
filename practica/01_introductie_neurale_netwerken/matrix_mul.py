import random

inputmat = [[1,1,1,1,0,1,1,1,1]]

low = 0
high =5
cols = 1
rows = 9

new = [random.choices(range(low,high), k=cols) for _ in range(rows)]
print(new)

outputCircle = [[0]]

for i in range(len(inputmat)):
 
    # iterating by column by B
    for j in range(len(new[0])):
 
        # iterating by rows of B
        for k in range(len(new)):
            outputCircle[i][j] += inputmat[i][k] * new[k][j]
 
for r in outputCircle:
    print(r)