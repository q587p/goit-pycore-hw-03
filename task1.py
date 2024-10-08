from datetime import datetime

"""
    Розраховує кількість днів між заданою датою та поточною датою.

    :param date: рядок дати у форматі 'РРРР-ММ-ДД'
    :return: ціле число, що вказує кількість днів до поточної дати
"""
def get_days_from_today(date):
    try:
        # Перетворення рядка дати на об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
        #print(input_date)
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

    # Отримання поточної дати без часу
    today = datetime.today().date()
    #print(today)

    # Розрахунок різниці між сьогоднішньою датою та заданою
    delta = (input_date.date() - today).days

    return delta

# Приклад використання
print(get_days_from_today("2023-10-08"))