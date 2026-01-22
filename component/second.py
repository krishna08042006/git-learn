def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide two numbers and return the result."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"


# Example usage
if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(6, 7))
    print(divide(20, 4))
    print(greet("Krish"))