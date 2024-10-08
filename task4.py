from datetime import datetime, timedelta

"""
    Визначає, кого з колег потрібно привітати з днем народження в найближчі 7 днів.

    :param users: список словників з інформацією про колег
    :return: список словників з іменами користувачів та датами привітань
"""
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертація дати народження зі строкового формату у datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Отримуємо день народження цього року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження в межах наступних 7 днів
        if today <= birthday_this_year <= today + timedelta(days=7):
            # Перевірка, чи попадає день народження на вихідний
            if birthday_this_year.weekday() in [5, 6]:  # 5 = субота, 6 = неділя
                # Переносимо на наступний понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Додаємо до списку результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.10.13"},
    {"name": "Jane Smith", "birthday": "1990.10.17"},
    {"name": "Alice Johnson", "birthday": "1992.10.18"},
    {"name": "Bob Brown", "birthday": "1988.10.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)