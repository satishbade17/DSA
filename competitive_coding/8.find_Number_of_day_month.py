def find_Number_of_day_month(month):
    if month in [1,3,5,7,8,10,12]:
        return '31 Days'
    
    elif month in [4,6,9,11]:
        return '30 Days'
    
    elif month==2:
        return '28 or 29 Days'
    
    else:
        return 'Invalid month'
month=int(input("Enter the month 1 to 12:-"))
print("days in month:",find_Number_of_day_month(month))
        