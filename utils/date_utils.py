from utils import logger


def is_leap(year: int) -> bool:
    """
    checks if the given year is leap

    Args:
        year (int): the year to be checked

    Returns:
        bool: True if year is leap else false
    """
    try:
        if (year % 400 == 0) and (year % 100 == 0):
            return True
        elif (year % 4 == 0) and (year % 100 != 0):
            return True
        return False
    except Exception as e:
        logger.log_message(
            message=f"Error in is_leap: {e.args}", level=1)


def validate_date(date_list: list) -> list:
    """
    validates each date from the list

    Args:
        date_list (list): list of strings as dates

    Returns:
        list: validated list of strings as dates
    """
    try:
        # valid date for each month
        month_days = {
            '1': 31,
            '2': 28,
            '3': 31,
            '4': 30,
            '5': 31,
            '6': 30,
            '7': 31,
            '8': 31,
            '9': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }

        for i in range(len(date_list)):
            # for each date, extract the date, month and year
            date = int (date_list[i][:2])
            month = int (date_list[i][3:5])
            year = int (date_list[i][6:10])

            valid_date = month_days[str(month)]
            # if its a leap year, 2nd month will have 1 extra day
            if is_leap(year=year) and month == 2:
                valid_date += 1
            # is date is invalid change month and validate it
            if date > valid_date:
                date = date - valid_date
                month += 1
                # is month is invalid, change year and validate it
                if month > 12:
                    year += 1
                date_list[i] = str(date)+'/'+str(month)+'/'+str(year)
        return date_list
    except Exception as e:
        logger.log_message(
            message=f"Error while validating date: {e.args}", level=1)