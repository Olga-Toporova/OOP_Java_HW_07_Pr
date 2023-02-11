import Try_input as t
import Calculator


class Complex():

    def new_complex_number(self, ch):
        calc = Calculator.Calculator()
        a = t.check_input_compl()  # создание комплексного числа

        if ch != "4":
            b = t.check_input_compl()
        else:
            b = t.div_zero_complex()  # проверка комплексного числа на 0

        calc.operation(ch, a, b)
