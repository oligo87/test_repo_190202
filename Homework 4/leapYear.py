def is_year_leap(year):
    if not (year % 400 == 0) and year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True
    else:
        is_leap = False
    return is_leap


if __name__ == "__main__":
    year = int(input('Input Year: '))
    leap = is_year_leap(year)
    print(f'Is year is leap: {leap}')
