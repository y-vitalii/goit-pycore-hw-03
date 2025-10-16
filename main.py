from datetime import datetime, timedelta 
import random 
import re


"""
Task 1
"""
DATE_FORMAT = '%Y-%m-%d';

def get_days_from_today(date: str):
    """
    Calculate the number of days between the current date and given.

    Args:
        date (str): The date string in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the current date and given.
    """
    try:
        time_difference = datetime.now() - datetime.strptime(date, DATE_FORMAT);
        print(time_difference.days)
        return time_difference.days
    except:
        print('Fromat data must be in fromat YYYY-MM-DD')

get_days_from_today('2025-10-15')   


"""
Task 2
"""
def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Generate a sorted list of unique random numbers

    Args:
        min (int): The minimum possible number (must be >= 1)
        max (int): The maximum possible number (must be <= 1000)
        quantity (int): The number of unique random numbers to generate

    Returns:
        list[int]: A sorted list containing unique random numbers between 'min' and 'max'.
    """
    
    if min < 1 or max > 1000 or min > max or min == max:
        print('Min value must be >= 1 and max value <= 1000 and not equal')
        return
    
    ticket_set = set()

    while len(ticket_set) < quantity:
        ticket_set.add(random.randrange(min, max + 1))

    print(sorted(ticket_set))
    return sorted(ticket_set)


get_numbers_ticket(100, 1000, 50)


"""
Task 3
"""
PHONE_CODE_UK = '+38'

def normalize_phone(phone_number: str):
    """
    Normalize a phone number
    """
    # only digits and + 
    s = re.sub(r"[^0-9+]", "", phone_number)

    if s.startswith("+"):
        normalized = s
    elif s.startswith(PHONE_CODE_UK.lstrip("+")):
        normalized = "+" + s
    elif s.startswith("0"):
        normalized = PHONE_CODE_UK + s

    return normalized


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


"""
Task 4
"""
def get_upcoming_birthdays(users):
    """
    Returns a list of users who have birthdays within the next 7 days
    """
    upcoming_birthdays = []
    current_date = datetime.today().date()

    for user in users:
        birthday_datetime = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_datetime = birthday_datetime.replace(year=current_date.year)

        if birthday_datetime.day < current_date.day:
            birthday_datetime = birthday_datetime.replace(year=current_date.year + 1)
        
        time_difference = birthday_datetime - current_date

        if 0 <= time_difference.days <= 7:
            if birthday_datetime.weekday() == 5:
                birthday_datetime += timedelta(days = 2)
            elif birthday_datetime.weekday() == 6:
                birthday_datetime += timedelta(days = 1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_datetime.strftime("%Y-%m-%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.20"},
    {"name": "Jane Smith", "birthday": "1990.10.22"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)