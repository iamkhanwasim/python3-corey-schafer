days = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """This function returns True if the year is a leap year
    or returns False"""
    
    return year % 4 == 0

def number_of_days(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month' 
    
    if month == 2 and is_leap(year):
        return 29
    
    return days[month-1]

# Function call
print("Number of days:",number_of_days(2022,0))
    