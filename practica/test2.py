
import random

matrix = [[1,1,1],
    [1,0,1],
    [1,1,1]]
rows = 2
columns = 9


    
weightMatrix = [[round(random.uniform(0, 1), 2) for _ in range(rows)] for _ in range(columns)]
print(weightMatrix)
transposedMatrix =list(map(list, zip(*matrix)))
flatMatrix = [[item for sub_list in transposedMatrix for item in sub_list]]
    
outputMatrix = [[round(sum(a*b for a,b in zip(A_row, B_col)), 2) for B_col in zip(*weightMatrix)] 
        for A_row in flatMatrix]

print(outputMatrix)
print(len(outputMatrix))
bias =[[0,0]]
output1 = outputMatrix[0][0]+bias[0][0]
output2 = outputMatrix[0][1]+bias[0][1]
print(output1)
print(output2)
e = 2.7182
softmax1= e**output1/(e**output1 +e**output2)
softmax2 = e**output2/(e**output1 +e**output2)
print(softmax1)
print(softmax2)
totalsoftmax = (softmax1 + softmax2)
print(totalsoftmax)

# def multiply(flatMatrix, weightMatrix):
#     outputMatrix = [[round(sum(a*b for a,b in zip(A_row, B_col)), 2) for B_col in zip(*weightMatrix)] 
#              for A_row in flatMatrix]
#     return outputMatrix    