# module used for increasing the simulator timer
# time is expressed in seconds
# could be improved by using DateTime


def increase_time(current_date, delta=1):
    """ increase timer(@param current_date) by delta(default set to 1) seconds """
    current_date = current_date + delta
    return current_date

