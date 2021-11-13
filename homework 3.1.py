# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


user_input_a = int(input("Введите число a:  "))
user_input_b = int(input("Введите число b:  "))
total = divide_func(user_input_a, user_input_b)
if total is not None:
    print(f"a разделить на b равно: {total}")
