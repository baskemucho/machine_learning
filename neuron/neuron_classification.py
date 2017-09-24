import math
import matplotlib.pyplot as plt

#sigmoid function
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

# neuron
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

# neural_network
class NeuralNetwork:
    w = [-0.5, 0.5]
    neuron = Neuron()

    def commit(self, input_data):
        self.neuron.reset()
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        return  self.neuron.getOutput()

refer_point_0 = 34.5
refer_point_1 = 137.5

trial_data = []
trial_data_file = open("trial_data", "r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0, float(line[1]) - refer_point_1])
trial_data_file.close()



neural_network = NeuralNetwork()


position_tokyo = [[], []]
position_kanagawa = [[], []]
for data in trial_data:
    if  neural_network.commit(data) < 0.5:
        position_tokyo[0].append(data[1] + refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)

plt.scatter(position_tokyo[0], position_tokyo[1], c = "red", label = "position", marker = "+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c = "green", label = "position", marker = "+")

plt.legend()
plt.show()
