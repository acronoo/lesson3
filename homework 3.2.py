# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_param(first_name, second_name, year, city, email, phone):
    print(f"Имя: {first_name}. Фамилия: {second_name}. Год рождения: {year}. Город проживания: {city}."
          f" Email: {email}. Телефон: {phone}")


user_param(second_name="Doe", year=1993, first_name="John", city="Mexico", email="john.doe@gmail.com", phone=9876543210)

