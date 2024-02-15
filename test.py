import json

import constants


class Layer:
    def __init__(self, neurons_number, previous_neurons, dummy_weight):
        self.neurons = self.create_neurons(neurons_number, previous_neurons, dummy_weight)

    def create_neurons(self, neurons_number, previous_neurons, dummy_weight):
        return [Neuron(i, previous_neurons, dummy_weight) for i in range(neurons_number)]

    def __repr__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)


class Neuron:
    def __init__(self, id, previous_neurons, dummy_weight):
        self.id = id
        self.neuron_connections = self.create_neuron_connections(previous_neurons, dummy_weight)
        self.value = self.calculate_value(previous_neurons)

    def create_neuron_connections(self, previous_neurons, dummy_weight):
        # Assuming 'previous_neurons' is a list of Neuron objects
        return [NeuronConnection(neuron, dummy_weight) for neuron in previous_neurons]

    def __repr__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)

    def calculate_value(self, previous_neurons):
        if not previous_neurons:



class NeuronConnection:
    def __init__(self, neuron: Neuron, weight: float):
        # Assuming 'neuron' should be represented by its ID or similar for JSON serialization
        self.neuron = neuron.id  # Store neuron ID instead of Neuron object to make it JSON serializable
        self.weight = weight

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)


network = [3, 2]
dummy_weight = 5
layers = []


def get_input_layer():
    # stworz layer generujac dummy dane z sensorów
    return Layer(constants.SENSORS_NUMBER, )

layers.append(get_input_layer())
previous_neurons = layers[0].neurons
for neurons_number in network:
    layer = Layer(neurons_number, previous_neurons, dummy_weight)
    previous_neurons = layer.neurons
    layers.append(layer)

print(layers)

