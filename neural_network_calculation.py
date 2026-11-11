class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def calculate_output(self, inputs):
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs))
        return weighted_sum


class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, inputs):
        return [neuron.calculate_output(inputs) for neuron in self.neurons]


class NeuralNetwork:
    """
    Simple linear neural network
    """
    def __init__(self, sensors, network_hidden_layers, weights):
        self.sensors = sensors
        self.network_layers = []
        if not self.validate_weights(network_hidden_layers, weights):
            raise ValueError("Invalid length of weights array.")
        self.network_layers = self.create_network(network_hidden_layers + [1], weights)

    def validate_weights(self, network_hidden_layers, weights):
        total_weights_needed = 0
        input_size = len(self.sensors)

        for layer_size in network_hidden_layers + [1]:
            total_weights_needed += layer_size * input_size
            input_size = layer_size

        return total_weights_needed == len(weights)

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
