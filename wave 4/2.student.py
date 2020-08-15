
def readable_timedelta(integer):
    days = integer%7
    week = integer//7
    print(f'{week} week(s) and {days} day(s)')


print(readable_timedelta(10))