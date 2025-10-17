from datetime import datetime, timedelta 


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