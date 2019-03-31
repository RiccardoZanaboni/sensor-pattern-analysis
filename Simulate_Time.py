import datetime as dt


def increase_time(current_date):
    delta = dt.timedelta(minutes=1)
    current_date = current_date + delta
    return current_date

