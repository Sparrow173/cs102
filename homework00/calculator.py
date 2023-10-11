"""
    Простая программа калькулятор
"""

import math
import typing as tp


def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    """_summary_

    Args:
        num_1 (float): первое число
        num_2 (float): второе число
        command (str): операция

    Returns:
        tp.Union[float, str]: результат или ошибку
    """
    result = None
    if command == "/" and num_2 == 0:  # проверка деления на ноль
        return "На ноль делить нельзя"
    # проверка на логарифм от отрицательного числа
    if command in ("ln", "ln") and num_1 <= 0:
        return "Нельзя посчитать логарифм"
    if command in duo:
        if command == "+":
            result = num_1 + num_2
        if command == "-":
            result = num_1 - num_2
        if command == "/":
            result = num_1 / num_2
        if command == "*":
            result = num_1 * num_2
        if command == "^":
            result = num_1**num_2
    if command in uno:
        if command == "**2":
            result = num_1**2
        if command == "sin":
            result = math.sin(num_1)
        if command == "cos":
            result = math.cos(num_1)
        if command == "tan":
            result = math.tan(num_1)
        if command == "ln":
            result = math.log2(num_1)
        if command == "lg":
            result = math.log10(num_1)
    if result is None:
        return f"Неизвестный оператор: {command!r}."
    return result


def get_param(prompt: str) -> float:  # функция получения числа
    """_summary_

    Args:
        prompt (str): подсказка пользователю

    Returns:
        float: полученное число
    """
    result = None
    while result is None:  # Повторяет до тех пор, пока не получится число
        try:  # Попробуем выполнить операцию
            result = float(input(prompt))
        except ValueError:  # Если возникла ошибка
            print("Ошибка ввода: Введите число")
    return result  # возвращаем результат


uno = ("sin", "tan", "cos", "ln", "lg", "**2")
duo = ("+", "-", "*", "/", "^")
nope = ("0",)

commands = uno + duo + nope

if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        COMMAND = ""
        RESULT = None
        NUM_1 = NUM_2 = NUM = 0.0  # инициализируем переменные
        # отсеиваем неправильные операции
        while (COMMAND := input("Введите операцию > ").strip().lower()) not in commands:  # noqa
            print("Ошибка, введите другую операцию")
        if COMMAND in duo:  # если команда с двумя операндами
            NUM_1 = get_param("Первое число > ")  # получаем первое число
            DONE = False  # устанавливаем флаг проверки допустимости операции
            while not DONE:
                NUM_2 = get_param("Второе число > ")  # получаем второе число
                # если равно нулю, выводим сообщение об ошибке
                if COMMAND in ["/"] and NUM_2 == 0:
                    print("На ноль делить нельзя")
                else:
                    DONE = True  # все нормально

            # получаем резальтат выислений
            RESULT = calc(NUM_1, NUM_2, COMMAND)
        elif COMMAND in uno:  # если команда с одним операндом
            DONE = False  # устанавливаем флаг проверки допустимости операции
            while not DONE:
                NUM = get_param("Введите число > ")  # получаем число
                # если значение равно нулю и логарифм
                if COMMAND in ["lg", "ln"] and NUM <= 0:
                    # сообщение об ршибке
                    print("Число может быть только положительным")
                else:
                    DONE = True  # все нормально
            RESULT = calc(NUM, 0, COMMAND)   # получаем резальтат выислений
        elif COMMAND == "0":  # если команда '0'
            break  # выходим
        print(RESULT)  # вывод результата вычислений
