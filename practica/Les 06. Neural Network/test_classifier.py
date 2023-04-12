from classifier import Matrix

# matrix = Matrix( 0, 5)

# matrix.getWeightMatrix()

# print(f'Rectangle color: {matrix.getWeightMatrix()}')

# matrix.outputCircle()

# print(f'Rectangle color: {matrix.outputCircle()}')
import random

inputmat = [[1,1,1,1,0,1,1,1,1]]

low = 0
high =5
cols = 1
rows = 9

new = [random.choices(range(low,high), k=cols) for _ in range(rows)]
print(new)

outputCircle = [[0]]

mat = Matrix()

mat.getmat()

print(f'Rectangle color: {mat.getmat()}')
