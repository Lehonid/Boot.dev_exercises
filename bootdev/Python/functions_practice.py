def to_celsius(f):
    c = 5/9 * (f - 32)
    return c 


# This function expects 1 arguments, and gets 1 arguments:

def hours_to_seconds(hours):
    return hours * 60 * 60

# mieux que 
def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds
