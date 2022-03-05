import speculate
import random

dataArray = [random.uniform(0, 1) for _ in range(252)]
speculate.New(dataArray)

print(":> Ready")