def convert_time(time, period):
    hour, minute = map(int, time.split(":"))

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour = hour + 12

    return f"{hour:02d}:{minute:02d}"


time = input("Enter time (HH:MM): ")
period = input("Enter AM or PM: ").upper()

result = convert_time(time, period)

print("24-hour format:", result)