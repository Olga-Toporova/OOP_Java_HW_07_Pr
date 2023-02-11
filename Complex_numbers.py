import Try_input as t
import Calculator


class Complex():

    def operation(self, ch):
        calc = Calculator.Calculator()

        a = t.check_input_compl() # создание комплексного числа

        if ch != "4":
            b = t.check_input_compl()
        else:
            b = t.div_zero_complex()  # проверка комплексного числа на 0

        if ch == "1":
            print(calc.add(a, b))
        if ch == "2":
            print(calc.subtract(a, b))
        if ch == "3":
            print(calc.multiply(a, b))
        if ch == "4":
            print(calc.divide(a, b))
