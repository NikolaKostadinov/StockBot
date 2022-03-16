import neuralnetwork as nn, numpy as np, matplotlib.pyplot as plt

layers = [24, 72, 216, 216, 72, 1]
bot = nn.NeuralNetwork(layers)
input = np.array([1 for _ in range(layers[0])])
want = np.array([1 for _ in range(layers[-1])])
n = 10*sum(layers)

y = []

output = bot.Forward(input)
err = bot.TotalError(want)
y.append(err)
print(f"Initial Error: {err}")
print(f"Initial Result: {output}")
bot.Backward(want)
for _ in range(n-1):
    output = bot.Forward(input)
    err = bot.TotalError(want)
    y.append(err)
    bot.Backward(want)    
print(f"Final Error: {err}")

output = bot.A[-1].tolist()
print(f"Final Result: {output}")

x = np.arange(0, len(y))
y = np.array(y)
plt.plot(x, y, color="red")
plt.show()