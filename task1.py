from datetime import datetime 


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
        return time_difference.days
    except:
        print('Fromat data must be in fromat YYYY-MM-DD')