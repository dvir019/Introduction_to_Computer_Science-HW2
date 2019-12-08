def main():
    day, month, year = get_date()
    difference = get_difference()
    new_day, new_month, new_year = get_new_date(day, month, year, difference)
    print_date(new_day, new_month, new_year)


def get_date():
    date_str = input("Enter a date:")
    date_list = date_str.split('/')
    day, month, year = [int(part_of_date) for part_of_date in date_list]
    return day, month, year


def get_difference():
    difference = int(input("Enter number of days:"))
    return difference


def get_new_date(day, month, year, difference):
    if (difference >= 0):
        return add_to_day(day, month, year, difference)
    return subtract_from_day(day, month, year, -difference)


def add_to_day(day, month, year, difference):
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
    while difference > 0:
        if day - difference > 0:
            day -= difference
            difference = 0
        else:
            difference -= day
            day, month, year = get_previous_month(year, month)

    return day, month, year


def get_next_month(year, month):
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    return day, month, year


def get_previous_month(year, month):
    if month > 1:
        month -= 1
    else:
        month = 12
        year -= 1

    day = get_number_of_days_in_month(year, month)
    return day, month, year


def is_leap_year(year):
    is_leap = False  # Assume it's not a leap year
    if year % 400 == 0:
        is_leap = True
    elif (year % 4 == 0) and (year % 100 != 0):
        is_leap = True
    return is_leap


def get_number_of_days_in_month(year, month):
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
    date = f"{day}/{month}/{year}"
    print(date)


if __name__ == '__main__':
    main()
