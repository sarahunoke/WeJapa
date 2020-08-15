def readable_timedelta(days):
    # insert your docstring here
    """ 
    A function that calculates the number of weeks and days in an integer
    
    Parameters: 
        days (int) : number
        
    Returns:
        a string containing the number of weeks and days in an integer
    
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)