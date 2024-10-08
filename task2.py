import random

"""
    Генерує набір унікальних випадкових чисел для лотерейного квитка.

    :param min: Мінімальне можливе число (не менше 1).
    :param max: Максимальне можливе число (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Список випадково вибраних, відсортованих чисел або пустий список.
"""
def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Повернення відсортованого списку
    return sorted(numbers)

# Приклади використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)