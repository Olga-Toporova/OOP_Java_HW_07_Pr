import Try_input as t
import Calculator
from sys import exit


class Main():

    @staticmethod
    def hello():
        print("Добро пожаловать в калькулятор!")
        print("Какую операцию хотите выполнить?\n"
              "1 - сложение\n"
              "2 - вычитание\n"
              "3 - умножение\n"
              "4 - деление")
        choice = t.choice()

        # if choice == "0":
        #     print("Выход из программы.\nДо свидания!")
        #     exit

        a, b = t.try_input(), t.try_input()
        calc = Calculator.Calculator()

        if choice == "1":
            print(calc.add(a, b))
        elif choice == "2":
            print(calc.subtract(a, b))
        elif choice == "3":
            print(calc.multiply(a, b))
        elif choice == "4":
            print(calc.divide(a, b))


Main.hello()
