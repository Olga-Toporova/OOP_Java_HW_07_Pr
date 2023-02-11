import Try_input as t
import Calculator


class Rational():

    def operation(self, ch):
        calc = Calculator.Calculator()

        a = t.try_input()
        
        if ch != "4":   # 4 - операция деления
            b = t.try_input()
        else:
            b = t.div_zero(t.try_input()) # проверка на 0

        if ch == "1":
            print(calc.add(a, b))
        if ch == "2":
            print(calc.subtract(a, b))
        if ch == "3":
            print(calc.multiply(a, b))
        if ch == "4":
            print(calc.divide(a, b))
