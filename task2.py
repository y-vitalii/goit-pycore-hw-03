import random 


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

    return sorted(ticket_set)