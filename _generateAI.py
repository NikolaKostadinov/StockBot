import speculate
import random
from termcolor import colored

dataArray = [random.uniform(0, 1) for _ in range(240)]
speculate.New(dataArray)

print(colored(":> Ready", "green"))