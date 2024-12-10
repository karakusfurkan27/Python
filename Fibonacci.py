import math

def fibonacci_pattern(n):
    a, b = 0, 1
    for i in range(n):
        x, y = int(math.cos(i) * b), int(math.sin(i) * b)
        print(" " * (x + 20) + "*")
        a, b = b, a + b

fibonacci_pattern(20)
