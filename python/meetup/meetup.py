from datetime import date
from calendar import monthrange


WEEKDAYS = ('sunday', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday')


def days_of_month(year, month):
    """Days of month as index of WEEKDAYS constant"""
    (first_day_of_month, days_in_month) = monthrange(year, month)

    return ([(first_day_of_month + day) % len(WEEKDAYS)
             for day in list(range(days_in_month+1))])


def get_possible_days(year, month, day):
    """Possible days as index of WEEKDAYS constant"""
    return ([i for i, x in enumerate(days_of_month(year, month)) 
        if WEEKDAYS[x] == day])


def validate_scheduled_day(scheduled_day, possible_days):
    schedule = {'1st': 0,
                '2nd': 1,
                '3rd': 2,
                '4th': 3,
                '5th':  4,
                'last': -1}
    try:
        return possible_days[schedule[scheduled_day]]
    except IndexError:
        raise Exception('Scheduled day is not available')


def meetup_day(year, month, day, scheduled_day):
    possible_days = get_possible_days(year, month, day.lower())

    if scheduled_day == 'teenth':
        for i in possible_days:
            if i >= 13 and i <= 19:
                return date(year, month, i)
    else:
        day = validate_scheduled_day(scheduled_day, possible_days)

        if day == 0:
            day = 7

        return date(year, month, day)