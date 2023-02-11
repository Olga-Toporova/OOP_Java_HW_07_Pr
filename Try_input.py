# Проверка корректности ввода выбора 1 (тип числа) в Main.menu
def choice_1():
    while True:
        try:
            op = input("Выберите опцию: ")
            if op.isdigit and int(op) in range(0, 3):
                return op
            else:
                print("Некорректный ввод, значение вне диапазона 0-2")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


# Проверка корректности ввода выбора 2 (тип операции) в Main.menu
def choice_2():
    while True:
        try:
            op = input("Выберите опцию: ")
            if op.isdigit and int(op) in range(0, 5):
                return op
            else:
                print("Некорректный ввод, значение вне диапазона 0-4")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


# Проверка корректности ввода числа
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


# Создание комплексного числа
def complex_number(a, b):
    return complex(a, b)


# Проверка корректного ввода комплексного числа
def check_input_compl():
    number1, number2 = try_input(), try_input()
    while True:
        try:
            compl_number = complex_number(number1, number2)
            return compl_number
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


# Проверка ввода нуля (для операции деления)
def div_zero(number):
    while number == 0:
        print("Делитель не может быть нулём!")
        number = try_input()
    return number


# Проверка ввода нуля (для операции деления комплексного числа)
def div_zero_complex():
    number1, number2 = div_zero(try_input()), div_zero(try_input())
    while True:
        try:
            compl_number = complex_number(number1, number2)
            return compl_number
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")
