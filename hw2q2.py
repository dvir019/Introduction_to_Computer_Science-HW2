def main():
    day, month, year = get_date()
    difference = get_difference()
    new_day, new_month, new_year = get_new_date(day, month, year)
    print_date(new_day, new_month, new_year)


def get_date():
    date_str = input("Enter a date:")
    date_list = date_str.split('/')
    day, month, year = [int(part_of_date) for part_of_date in date_list]
    return day, month, year


def get_difference():
    difference = int(input("Enter number of days:"))
    return difference


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
