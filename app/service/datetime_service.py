import datetime


def check_datetime(created_at):
    now = datetime.datetime.now()
    compared = datetime.datetime(now.year, now.month, now.day-1, now.hour, now.minute, now.second)
    if (created_at.day == compared.day and created_at.hour >= compared.hour) or created_at.day > compared.day:
        return True
    else:
        return False
