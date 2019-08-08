import random

randomArray = []
uniformArray = []
gaussianArray = []

for i in range(1,100):
    randomArray.append(random.random())
    uniformArray.append(random.uniform(1,100))
    gaussianArray.append(random.gauss(1,100))

print(randomArray)
print(uniformArray)
print(gaussianArray)