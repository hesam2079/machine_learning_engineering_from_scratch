class Layer:
    def __init__(self, input_dim, output_dim, activation=lambda x: x):
        self.input_dim = int(input_dim)
        self.output_dim = int(output_dim)
        self.activation = activation
        self.weights = np.random.randn(input_dim, output_dim) * 0.01
        self.biases = np.zeros(output_dim)

    def forward(self, input):
        if input.shape != (self.input_dim,):
            raise ValueError(f"Input shape {input.shape} does not match layer input shape {(self.input_dim,)}")
