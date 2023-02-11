import Try_input as t


class Calculator:

# Вывод на экран результата
    def operation(self, ch, a, b):
        if ch == "1":
            print(Calculator.add(self, a, b))
        if ch == "2":
            print(Calculator.subtract(self, a, b))
        if ch == "3":
            print(Calculator.multiply(self, a, b))
        if ch == "4":
            print(Calculator.divide(self, a, b))


# Вычисления
    def add(self, a, b):
        return f"{a} + {b} = {a + b}"

    def subtract(self, a, b):
        return f"{a} - {b} = {a - b}"

    def multiply(self, a, b):
        return f"{a} * {b} = {a * b}"

    def divide(self, a, b):
        return f"{a} / {b} = {a / b}"
