import datetime


def check_datetime(created_at):
    """
    @param now:        the datetime representation of current datetime   
    @param compared:    the datetime representation of time 24 hours ago     
    @param created_at:    the datetime representation of creation of product 
    @return:            the boolean representation of date is in last 24 hours
    """
    now = datetime.datetime.now()
    compared = datetime.datetime(now.year, now.month, now.day-1, now.hour, now.minute, now.second)
    if (created_at.day == compared.day and created_at.hour >= compared.hour) or created_at.day > compared.day:
        return True
    else:
        return False
