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
    if command == "/" and num_2 == 0:
        return "На ноль делить нельзя"
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


def get_param(prompt: str) -> float:
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
    return result


uno = ("sin", "tan", "cos", "ln", "lg", "**2")
duo = ("+", "-", "*", "/", "^")
nope = ("0",)

commands = uno + duo + nope

if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        COMMAND = ""
        RESULT = None
        NUM_1 = NUM_2 = NUM = 0.0
        # отсеиваем неправильные операции
        while (COMMAND := input("Введите операцию > ").strip().lower()) not in commands:  # noqa
            print("Ошибка, введите другую операцию")
        if COMMAND in duo:
            NUM_1 = get_param("Первое число > ")
            DONE = False
            while not DONE:
                NUM_2 = get_param("Второе число > ")
                if COMMAND in ["/"] and NUM_2 == 0:
                    print("На ноль делить нельзя")
                else:
                    DONE = True
            # num_1 = float(input("Первое число > "))
            # num_2 = float(input("Второе число > "))
            RESULT = calc(NUM_1, NUM_2, COMMAND)
        elif COMMAND in uno:
            DONE = False
            while not DONE:
                NUM = get_param("Введите число > ")
                if COMMAND in ["lg", "ln"] and NUM <= 0:
                    print("Число может быть только положительным")
                else:
                    DONE = True
            RESULT = calc(NUM, 0, COMMAND)
        elif COMMAND == "0":
            break
        print(RESULT)
