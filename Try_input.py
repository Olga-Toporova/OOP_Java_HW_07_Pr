def choice():
    while True:
        try:
            nr = input("Выберите опцию: ")
            if nr.isdigit and int(nr) in range(1, 5):
                return nr
            else:
                print("Некорректный ввод, значение вне диапазона 1-4")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


def try_input():
    while True:
        try:
            number = input('Введите значение: ')
            if number.count(".") or number.count(","):
                number = float(number)
            else:
                number = int(number)
            return number
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


# def complex_number(a, b):
#     return complex(a, b)


# def check_input_compl():
#     number1, number2 = try_input(), try_input()
#     while True:
#         try:
#             compl_number = complex_number(number1, number2)
#             return compl_number
#         except ValueError:
#             print("Неверное значение, попробуйте еще раз.")


def div_zero(number):
    while number == 0:
        print("Делитель не может быть нулём!")
        number = try_input()
    return number


# def div_zero_complex():
#     number1, number2 = div_zero(), div_zero()
#     while True:
#         try:
#             compl_number = complex_number(number1, number2)
#             return compl_number
#         except ValueError:
#             print("Неверное значение, попробуйте еще раз.")
