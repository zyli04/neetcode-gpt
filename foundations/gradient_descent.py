class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        def obj(x):
            return x**2
        # Derivative:         f'(x) = 2x
        def derivative(x):
            return 2*x
        # Update rule:        x = x - learning_rate * f'(x)
        def update(x, learning_rate, iterations):
            for i in range(iterations):
                x -= learning_rate * derivative(x)
            return x
        # Round final answer to 5 decimal places
        return round(update(init, learning_rate, iterations), 5)
