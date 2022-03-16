import os

print("\n******* IT'S ABOUT DRIVE *******\n")

path = "trainbot.py"
n = 2

for index in range(1, n+1):
    print(f"===========  <{index}>  ===========")
    os.system(f"python {path}")
    print("<END>\n")
    
print("******* IT'S ABOUT POWER *******")