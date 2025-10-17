import re


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