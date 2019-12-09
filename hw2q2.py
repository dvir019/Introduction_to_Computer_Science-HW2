def main():
    day, month, year = get_date()
    difference = get_difference()
    is_valid = is_date_valid(day, month, year)
    if is_valid:
        new_day, new_month, new_year = get_new_date(day, month, year, difference)
        print_date(new_day, new_month, new_year)
    else:
        print_invalid_date()


def get_date():
    """
    Gets a date from the user in the format day/month/year,
    splits it into day, month and year, and returns them.

    :return: The day, month and year
    :rtype: tuple[int, int, int]
    """
    date_str = input("Enter a date:")
    date_list = date_str.split('/')
    day, month, year = [int(part_of_date) for part_of_date in date_list]
    return day, month, year


def get_difference():
    """
    Gets the day difference from the user, and returns it as an integer.

    :return: The day difference
    :rtype: int
    """
    difference = int(input("Enter number of days:"))
    return difference


def is_date_valid(day, month, year):
    """
    Checks if a given date is valid, and returns the result.

    :param day: The day of the date
    :type day: int
    :param month: The month of the date
    :type month: int
    :param year: The year of the date
    :type year: int

    :return: Whether or not the day is valid
    :rtype: bool
    """
    is_valid = False  # Assume the date is invalid
    days_in_month = get_number_of_days_in_month(year, month)
    if (day > 0) and (day <= days_in_month) and (month > 0) and (month <= 12):  # Valid date
        is_valid = True

    return is_valid


def get_new_date(day, month, year, difference):
    """
    Calculates the new date according to the given date and the given day difference,
    and returns the new date.

    :param day: The day of the date
    :type day: int
    :param month: The month of the date
    :type month: int
    :param year: The year of the date
    :type year: int
    :param difference: The day difference
    :type difference: int

    :return: The new date
    :rtype: tuple[int, int, int]
    """
    if difference >= 0:
        return add_to_day(day, month, year, difference)
    return subtract_from_day(day, month, year, -difference)


def add_to_day(day, month, year, difference):
    """
    Adds the day difference to the date, and returns the new date.

    :param day: The day of the date
    :type day: int
    :param month: The month of the date
    :type month: int
    :param year: The year of the date
    :type year: int
    :param difference: The day difference (A non-negative integer)
    :type difference: int

    :return: The new date
    :rtype: tuple[int, int, int]
    """
    while difference > 0:
        days_in_month = get_number_of_days_in_month(year, month)
        if day + difference <= days_in_month:
            day += difference
            difference = 0
        else:
            difference = difference - (days_in_month - day) - 1
            day, month, year = get_next_month(year, month)

    return day, month, year


def subtract_from_day(day, month, year, difference):
    """
    Subtract the day difference from the date, and returns the new date.

    :param day: The day of the date
    :type day: int
    :param month: The month of the date
    :type month: int
    :param year: The year of the date
    :type year: int
    :param difference: The day difference (A positive integer)
    :type difference: int

    :return: The new date
    :rtype: tuple[int, int, int]
    """
    while difference > 0:
        if day - difference > 0:
            day -= difference
            difference = 0
        else:
            difference -= day
            day, month, year = get_previous_month(year, month)

    return day, month, year


def get_next_month(year, month):
    """
    Gets the date of the first day of the consecutive month of a given month in a given year.

    :param year: The year
    :type year: int
    :param month: The month
    :type month: int

    :return: The date of the first day of the consecutive month
    :rtype: tuple[int, int, int]
    """
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

    return day, month, year


def get_previous_month(year, month):
    """
    Gets the date of the last day of the previous month of a given month in a given year.

    :param year: The year
    :type year: int
    :param month: The month
    :type month: int

    :return: The date of the last day of the previous month
    :rtype: tuple[int, int, int]
    """
    if month > 1:
        month -= 1
    else:
        month = 12
        year -= 1

    day = get_number_of_days_in_month(year, month)

    return day, month, year


def is_leap_year(year):
    """
    Checks if a given year is a leap year, and returns the result.

    :param year: The year
    :type year: int

    :return: Whether or not the year is a leap year
    :rtype: bool
    """
    is_leap = False  # Assume it's not a leap year
    if year % 400 == 0:
        is_leap = True
    elif (year % 4 == 0) and (year % 100 != 0):
        is_leap = True
    return is_leap


def get_number_of_days_in_month(year, month):
    """
    Gets the number of days in a given month of a given year.

    :param year: The year
    :type year: int
    :param month: The month
    :type month: int

    :return: The number of days in the month
    :rtype: int
    """
    days_with_thirty_days = [4, 6, 9, 11]
    number_of_days = 31
    if month in days_with_thirty_days:
        number_of_days = 30
    elif month == 2:
        if is_leap_year(year):
            number_of_days = 29
        else:
            number_of_days = 28

    return number_of_days


def print_date(day, month, year):
    """
    Prints a given date in the format day/month/year.

    :param day: The day of the date
    :type day: int
    :param month: The month of the date
    :type month: int
    :param year: The year of the date
    :type year: int
    """
    date = f"{day}/{month}/{year}"
    print(date)


def print_invalid_date():
    """
    Prints that the given date is invalid.
    """
    message = "The given date is invalid."
    print(message)


if __name__ == '__main__':
    main()
