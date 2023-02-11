import Try_input as t
import Rational_numbers
import Complex_numbers
from sys import exit


class Main():

    @staticmethod
    def menu():
        print("С какими числами будете работать?\n"
              "1 - рациональные\n"
              "2 - комплексные\n"
              "0 - выход из программы")
        ch1 = t.choice_1()
        if ch1 == "0":
            print("Выход из программы.\nДо свидания!")
            exit(1)

        print("Какую операцию хотите выполнить?\n"
              "1 - сложение\n"
              "2 - вычитание\n"
              "3 - умножение\n"
              "4 - деление\n"
              "0 - возврат в предыдущее меню")
        ch2 = t.choice_2()

        # Перезапуск
        if ch2 == "0":
            Main.menu()
        else:
            # Переход к рациональным числам
            if ch1 == "1":
                calc = Rational_numbers.Rational()
                calc.new_number(ch2)
                Main.menu()
            # Переход к комплексным числам
            elif ch1 == "2":
                calc = Complex_numbers.Complex()
                calc.new_complex_number(ch2)
                Main.menu()


Main.menu()
