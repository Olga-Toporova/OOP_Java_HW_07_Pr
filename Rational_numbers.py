import Try_input as t
import Calculator


class Rational():

    def new_number(self, ch):
        calc = Calculator.Calculator()
        a = t.try_input()

        if ch != "4":  # 4 - операция деления
            b = t.try_input()
        else:
            b = t.div_zero(t.try_input())  # проверка на 0

        calc.operation(ch, a, b)
