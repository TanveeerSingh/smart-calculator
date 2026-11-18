"""Smart Calculator - UCS745 Lab Assignment Q1"""

def welcome_message():
    return "Hello! Welcome to Smart Calculator v2.0"

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(welcome_message())
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("20 / 5 =", divide(20, 5))
