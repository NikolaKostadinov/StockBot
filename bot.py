import enum
from stock import *

# Test Tesla Stock Data
ElonMusk = Stock("TSLA")

# Simple Average Prediction
sum, sigma = 0, 0
for index, this in enumerate(ElonMusk.closeChange):
    sum += this/len(ElonMusk.closeChange)
    sigma += this/(len(ElonMusk.closeChange)+1)
closeChangeNew = (sum - sigma)*(len(ElonMusk.closeChange)+1)
closeValueNew = ElonMusk.closeValues[-1] + closeChangeNew

sum, sigma = 0, 0
for index, this in enumerate(ElonMusk.openChange):
    sum += this/len(ElonMusk.openChange)
    sigma += this/(len(ElonMusk.openChange)+1)
openChangeNew = (sum - sigma)*(len(ElonMusk.openChange)+1)
openValueNew = ElonMusk.openValues[-1] + openChangeNew

sum, sigma = 0, 0
for index, this in enumerate(ElonMusk.highChange):
    sum += this/len(ElonMusk.highChange)
    sigma += this/(len(ElonMusk.highChange)+1)
highChangeNew = (sum - sigma)*(len(ElonMusk.highChange)+1)
highValueNew = ElonMusk.highValues[-1] + highChangeNew

sum, sigma = 0, 0
for index, this in enumerate(ElonMusk.lowChange):
    sum += this/len(ElonMusk.lowChange)
    sigma += this/(len(ElonMusk.lowChange)+1)
lowChangeNew = (sum - sigma)*(len(ElonMusk.lowChange)+1)
lowValueNew = ElonMusk.lowValues[-1] + lowChangeNew

print(f"New Close: {closeValueNew}")
print(f"New Open: {openValueNew}")
print(f"New High: {highValueNew}")
print(f"New Low: {lowValueNew}")

# Convert To JSON
ElonMusk.ToJSON()