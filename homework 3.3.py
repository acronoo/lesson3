# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    x = [a, b, c]
    print(x)
    x.sort(reverse=True)
    print(x)
    return x[0] + x[1]


summary = my_func(10, 30, 60)
print(summary)
