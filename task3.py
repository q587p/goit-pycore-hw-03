import re

"""
    Нормалізує телефонний номер до стандартного формату.

    :param phone_number: рядок з телефонним номером у різних форматах
    :return: нормалізований телефонний номер у вигляді рядка
"""
def normalize_phone(phone_number):
    # Видалення зайвих символів, залишаючи тільки цифри та символ '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())

    # Додавання міжнародного коду, якщо його немає
    if cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    elif cleaned_number.startswith('+'):
        pass  # Міжнародний код вже є
    else:
        cleaned_number = '+380' + cleaned_number.lstrip('0') # для України

    return cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)