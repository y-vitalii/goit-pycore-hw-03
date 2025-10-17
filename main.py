from task1 import get_days_from_today
from task2 import get_numbers_ticket
from task3 import normalize_phone
from task4 import get_upcoming_birthdays


# Task 1
print(get_days_from_today('2025-10-15'))   

# Task 2
print(get_numbers_ticket(100, 1000, 50))

# Task 3
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

# Task 4
users = [
    {"name": "John Doe", "birthday": "1985.10.20"},
    {"name": "Jane Smith", "birthday": "1990.10.22"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)