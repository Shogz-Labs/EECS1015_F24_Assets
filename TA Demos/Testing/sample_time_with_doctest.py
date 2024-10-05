import doctest
def get_time_format(seconds: int) -> str:
    """
    Convert a number of seconds into a string formatted as hh:mm:ss.
    >>> get_time_format(0)
    '00:00:00'
    >>> get_time_format(59)
    '00:00:59'
    >>> get_time_format(60)
    '00:01:00'
    >>> get_time_format(90061)
    '01:01:01'
    """
    clock_seconds = seconds % 60
    clock_minutes = (seconds // 60) % 60 
    clock_hours = ((seconds // 60) // 60) % 24 
    return f'{clock_hours:02}:{clock_minutes:02}:{clock_seconds:02}'

doctest.testmod()