import streamlit as st
import numpy as np

# Artificial Neural Network class with backpropagation algorithm
class NeuralNetwork:
    def __init__(self):
        # Initialize weights and biases
        self.weights = np.random.rand(2, 2)
        self.biases = np.random.rand(2, 1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feedforward(self, inputs):
        # Compute feedforward
        self.hidden = self.sigmoid(np.dot(self.weights, inputs) + self.biases)
        return self.hidden

    # Implement backpropagation algorithm to update weights and biases
    def train(self, inputs, targets, learning_rate):
        # Feedforward
        self.output = self.feedforward(inputs)
        # Compute error
        self.error = targets - self.output
        # Update weights and biases
        self.weights += learning_rate * np.dot((self.error * self.output * (1 - self.output)), inputs.T)
        self.biases += learning_rate * (self.error * self.output * (1 - self.output))

# Streamlit app
def main():
    st.title("Neural Network Backpropagation Demo")

    # Initialize neural network
    neural_network = NeuralNetwork()

    # Input form for dataset
    st.subheader("Enter Dataset")
    dataset_input = st.text_area("Enter dataset (one row per line)", "0.1, 0.2\n0.3, 0.4")

    # Print dataset button
    if st.button("Print Dataset"):
        dataset = []
        lines = dataset_input.strip().split("\n")
        for line in lines:
            data = [float(x.strip()) for x in line.split(",")]
            dataset.append(data)
        st.subheader("Dataset:")
        st.write(dataset)

    # Input form for training
    st.subheader("Input Data")
    input_data = st.text_input("Enter input data (comma separated)", "0.1, 0.2")

    if st.button("Train Neural Network"):
        # Split input data and convert to numpy array
        inputs = np.array([float(x.strip()) for x in input_data.split(",")]).reshape(-1, 1)
        # Dummy target data for demonstration
        targets = np.array([[0.9], [0.1]])
        # Train neural network
        neural_network.train(inputs, targets, learning_rate=0.1)
        st.success("Neural network trained successfully!")

    # Make predictions
    if st.button("Make Predictions"):
        inputs = np.array([float(x.strip()) for x in input_data.split(",")]).reshape(-1, 1)
        predictions = neural_network.feedforward(inputs)
        st.subheader("Predictions")
        st.write(predictions)

if __name__ == "__main__":
    main()
