class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def calculate_output(self, inputs):
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs))
        return self.relu(weighted_sum)

    @staticmethod
    def relu(x):
        return max(0, x)


class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, inputs):
        return [neuron.calculate_output(inputs) for neuron in self.neurons]


class NeuralNetwork:
    def __init__(self, sensors, network_hidden_layers, weights):
        self.sensors = sensors
        # Ensure the last layer is always a single-neuron layer for output
        self.network_layers = self.create_network(network_hidden_layers + [1], weights)

    def create_network(self, network_hidden_layers, weights):
        network = []
        weight_index = 0
        input_size = len(self.sensors)

        for layer_size in network_hidden_layers:
            neurons = []
            for _ in range(layer_size):
                neuron_weights = weights[weight_index:weight_index + input_size]
                neurons.append(Neuron(neuron_weights))
                weight_index += input_size
            network.append(Layer(neurons))
            input_size = layer_size
        return network

    def calculate(self):
        inputs = self.sensors
        for layer in self.network_layers:
            outputs = layer.forward(inputs)
            inputs = outputs
        return outputs


sensors = [54, 23, 31]
network_hidden_layers = [2, 3]
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

nn = NeuralNetwork(sensors, network_hidden_layers, weights)
output = nn.calculate()
print(output)
