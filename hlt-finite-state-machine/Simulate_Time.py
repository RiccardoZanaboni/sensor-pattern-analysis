import datetime as dt


def increase_time(current_date):
    """ function which simulate time """

    delta = dt.timedelta(minutes=1)
    current_date = current_date + delta
    return current_date

