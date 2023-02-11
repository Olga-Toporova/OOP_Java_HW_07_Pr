import Try_input as t

class Calculator:

    def add(self, a, b):
        return f"{a} + {b} = {a + b}"


    def subtract(self, a, b):
        return f"{a} - {b} = {a - b}"


    def multiply(self, a, b):
        return f"{a} * {b} = {a * b}"


    def divide(self, a, b):
        b = t.div_zero(b)
        return f"{a} / {b} = {a / b}"
