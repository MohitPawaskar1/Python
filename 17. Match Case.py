'''
    The match-case statement, introduced in Python 3.10, is used for structural pattern matching. 
    
    It is similar to switch statements in other languages but much more powerful.


'''
def http_status(status):
    match status:
        case 200:
            return "OK"
        
        case 404:
            return "Not Found"
        
        case 500:
            return "Internal Server Error"
        
        case _:
            return "Unknown Status"
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(900))




def check_number(num):
    match num:
        case x if x > 0:
            return "Positive"
        case x if x < 0:
            return "Negative"
        case _:
            return "Zero"

print(check_number(-5))  # Output: Negative
print(check_number(5))  # Output: Positive
print(check_number(0))  # Output: Zero




def get_day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(get_day_name(7))  # Output: Wednesday
