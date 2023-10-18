import datetime
from datetime import date


# BDD
def get_date(days_delta=0, edit_format=True, day_start_from=date.today()):
    day = day_start_from
    if edit_format:
        return (day - datetime.timedelta(days=days_delta)).strftime("%d/%m/%Y")
    return day - datetime.timedelta(days=days_delta)


def month_name(month=1):
    months = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    if not isinstance(month, int):
        return 'err'
    if month not in months:
        return 'err'
    return months[month]


# TDD
def month_short_name(month=1):
    months = {1: "янв", 2: "фев", 3: "мар", 4: "апр", 5: "май", 6: "июн", 7: "июл", 8: "авг", 9: "сен", 10: "окт", 11: "ноя", 12: "дек"}
    if not isinstance(month, int):
        return 'err'
    if month not in months:
        return 'err'
    return months[month]


def get_quarter(day=date.today()):
    day = day.replace(day=1)
    month = day.month
    if month in [3, 6, 9, 12]:
        return day
    if month in [1, 4, 7, 10]:
        return prev_month(day)
    if month in [2, 5, 8, 11]:
        return prev_month(prev_month(day))


# TDD
def quarter_name(month=12):
    if month not in range(12):
        return "err"
    quarters = ["Зима", "Весна", "Лето", "Осень", "Зима"]
    return quarters[month // 3]


# BDD
def prev_month(day=date.today()):
    month = day.month - 1
    if month == 0:
        day = day.replace(year=day.year - 1, month=12)
    else:
        day = day.replace(month=day.month - 1)
    return day

